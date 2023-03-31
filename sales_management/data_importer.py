from decimal import Decimal
import json
import logging
from typing import Any, Callable, Dict, List, Tuple, Type, Union, cast
from sales_management import models
from django.db import models as django_models, transaction
import os
from sales_management.IMPORT_CONFIGS import IMPORT_CONFIGS
from sales_management.utils import parse_datetime

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


class DataImporter():
    """
    A class to import data from JSON files into the sales management system.
    """

    def import_data_files(self, directory_path: str) -> None:
        """
        Import data from JSON files into the sales management system.

        The directory path must meet the following requirements:
        1. The directory must contain a JSON file for each model to import.
        2. The name of each JSON file must match the name of the model to import.

        The import process follows the steps of the import_data method

        Args:
            directory_path (str): The directory path to search for JSON files.
        """
        data = self._read_files(directory_path)
        self.import_data(data)

    @transaction.atomic
    def import_data(self, data: Dict[str, Any]) -> None:
        """
        Import data into the sales management system using the provided data dictionary.

        The data dictionary must meet the following requirements:
        1. Contain a key for each model to import.
        2. The value of each key should be a list of dictionaries containing the data to import for that model.

        The import process follows these steps:
        1. The import is performed in the order of the configurations in the IMPORT_CONFIGS list.
        2. The import is performed in a transaction. If an error occurs during the import, the database will be rolled back to its original state.

        Args:
            data (Dict[str, Any]): A dictionary containing the data to import.
        """
        global_id_map: Dict[str, Dict[str, int]] = {}

        try:
            for config in IMPORT_CONFIGS:
                target_name: str = config["target_name"]
                local_id_map: Dict[str, int] = {}
                if target_name in data:
                    field_map = config["field_map"]
                    src_pk = self._find_data_record_pk(field_map)
                    model = getattr(models, target_name)
                    local_id_map = self._import_records(
                        data[target_name], field_map, src_pk, global_id_map, model)

                global_id_map[target_name] = local_id_map

        except Exception as e:
            logger.error(e)
            raise Exception(f"import error:{e}")

    def clean_up(self):
        """
        Clean up the database after importing data. This method deletes all records from the models specified in the IMPORT_CONFIGS list.
        """
        for config in IMPORT_CONFIGS:
            target_name: str = config["target_name"]
            model = getattr(models, target_name)
            model.objects.all().delete()

    def _read_files(self, directory_path: str) -> Dict[str, Any]:
        """
        Read the content of the JSON files in the specified directory.

        Args:
            directory_path (str): The directory path to search for JSON files.
            return (Dict[str, Any]): A dictionary containing the content of the JSON files.
        """
        data = {}
        for target_name, data_file_path in self._search_data_files(directory_path):
            data[target_name] = self._read_file(data_file_path)
        return data

    def _read_file(self, file_path: str) -> Any:
        """
        Read the content of the specified JSON file.

        Args:
            file_path(str): The path of the JSON file to read.
            return (Any): The content of the JSON file.
        """
        try:
            with open(file_path, encoding="UTF-8") as f:
                content = f.read()
                content = self.preprocess(content)
                return json.loads(content)
        except FileNotFoundError as file_not_found_error:
            logger.error(file_not_found_error)
            raise Exception(f"file not found:{file_path}")
        except json.JSONDecodeError as json_error:
            logger.error(json_error)
            raise Exception((f"json decode error:{file_path}\n"
                             f"msg:{json_error.msg}\n"
                             f"lineno:{json_error.lineno} colno:{json_error.colno}"))

    def preprocess(self, content: str) -> str:
        """
        Preprocess the content of the JSON file.

        Args:
            content (str): The content of the JSON file.
            return (str): The preprocessed content.
        """
        # escape backslash
        content = content.replace('\\', '\\\\')
        return content

    def _search_data_files(self, path: str) -> List[Tuple[str, str]]:
        """
        Search for JSON data files in the specified path and return their file paths.

        Args:
            path (str): The directory path to search for JSON files.
            return (List[Tuple[str, str]]): A list of tuples containing the target name and file path of each JSON file found.
        """
        # enum all file names in `path`
        capital_data_file_names = [name.upper()
                                   for name, ext in
                                   [os.path.splitext(file_name)
                                    for file_name in os.listdir(path)]
                                   if ext == ".json"]

        target_names = {config["target_name"] for config in IMPORT_CONFIGS}

        # if there is a file name that is not in `IMPORT_CONFIGS`, raise an error
        diff = set(capital_data_file_names).difference({name.upper() for name in target_names})
        if len(diff) != 0:
            raise Exception(f"invalid data file names:{diff}")

        # build file paths in the order of `import_configs`
        data_file_paths = [(target_name, os.path.join(path, target_name + ".json")) for target_name in target_names]
        
        return data_file_paths

    def _import_records(self, records: List[Dict[str, str]], field_map: Dict[str, Union[str, Tuple[str, str]]], record_pk: str, global_id_map: Dict[str, Dict[str, int]], model) -> Dict[str, int]:
        """
        Import records into the specified model using the provided configuration.

        Args:
            records (List[Dict[str, str]]): A list of dictionaries containing the data to import for the model.
            field_map (Dict[str, Union[str, Tuple[str, str]]]): A dictionary containing the mapping between the model fields and the data fields.
            record_pk (str): The name of the primary key field in the data record.
            global_id_map (Dict[str, Dict[str, int]]): A dictionary containing the mapping between the primary key values in the data records and the primary key values in the database.
            model: The model to import the data into.
            return (Dict[str, int]): A dictionary containing the mapping between the primary key values in the data records and the primary key values in the database.
        """
        local_id_map = {}

        for record in records:
            params = {model_field_name: self._get_model_value(record, data_field_name, model, model_field_name, global_id_map)
                      for model_field_name, data_field_name in field_map.items()
                      if model_field_name != "pk"}

            s = model.objects.create(**params)
            if record_pk != "":
                local_id_map[record[record_pk]] = s.pk

        return local_id_map

    def _get_model_value(self, record: Dict[str, str], record_field_name: Union[str, Tuple[str, str]], model, model_field_name: str, global_id_map: Dict[str, Dict[str, int]]) -> Any:
        """
        Get the value for a model field from a data record.

        Args:
            record (Dict[str, str]): A dictionary containing the data to import for the model.
            record_field_name (Union[str, Tuple[str, str]]): The name of the field in the data record.
            model: The model to import the data into.
            model_field_name (str): The name of the field in the model.
            global_id_map (Dict[str, Dict[str, int]]): A dictionary containing the mapping between the primary key values in the data records and the primary key values in the database.
            return (Any): The value for the model field.
        """
        data_value = self._record_field_value(
            record, record_field_name, global_id_map)
        model_field = self._model_field(model, model_field_name)
        return self._convert_value(data_value, model_field)

    def _find_data_record_pk(self, field_map: Dict[str, Union[str, Tuple[str, str]]]) -> str:
        """
        Find the primary key field in the data record based on the provided configuration.

        Args:
            field_map (Dict[str, Union[str, Tuple[str, str]]]): A dictionary containing the mapping between the model fields and the data fields.
            return (str): The name of the primary key field in the data record.
        """
        return cast(str, next((src_field
                               for dst_field, src_field in field_map.items()
                               if dst_field == "pk"), ""))

    def _model_field(self, model, model_field_name: str) -> django_models.Field:
        """
        Get the model field object for the specified model and field name.

        Args:
            model: The model to import the data into.
            model_field_name (str): The name of the field in the model.
        """
        attr = getattr(model, model_field_name)
        field = attr.field
        return field

    def _record_field_value(self, record: Dict[str, str], field_name: Union[str, Tuple[str, str]], global_id_map: Dict[str, Dict[str, int]]) -> Any:
        """
        Get the value for a field from a data record.

        Args:
            record (Dict[str, str]): A dictionary containing the data to import for the model.
            field_name (Union[str, Tuple[str, str]]): The name of the field in the data record.
            global_id_map (Dict[str, Dict[str, int]]): A dictionary containing the mapping between the primary key values in the data records and the primary key values in the database.
            return (Any): The value for the field.
        """
        if isinstance(field_name, tuple):
            # if src_field is foreign key, return object if exists
            if field_name[0].startswith("[") and field_name[0].endswith("]"):
                model_name = field_name[0][1:-1]
                id_field_name = field_name[1]

                if record[id_field_name] not in global_id_map[model_name]:
                    return None

                id = global_id_map[model_name][record[id_field_name]]
                model = getattr(models, model_name)
                return model.objects.get(id=id)

            # if src_field is tuple and return tuple of values
            return tuple([record[f] for f in field_name])
        return record[field_name]

    def _convert_value(self, record_value: str, model_field: django_models.Field) -> Any:
        """
        Convert a data value to the appropriate type for the specified model field.

        Args:
            record_value (str): The value from the data record.
            model_field (django_models.Field): The model field to convert the value to.
            return (Any): The converted value.
        """
        value_converters: Dict[Type[django_models.Field], Callable[[str], Any]] = {
            django_models.CharField: lambda x: x if x != "" else "",
            django_models.IntegerField: lambda x: int(x) if x != "" else 0,
            django_models.DecimalField: lambda x: Decimal(x) if x != "" else Decimal(0),
            django_models.DateField: parse_datetime,
            django_models.DateTimeField: lambda x: parse_datetime(x) if not isinstance(x, tuple) else parse_datetime(*x),
            django_models.BooleanField: lambda x: True if x == "1" or x.upper() == "TRUE" else False,
            django_models.ForeignKey: lambda x: x,
            django_models.BigIntegerField: lambda x: int(x) if x != "" else 0,
        }
        return value_converters[type(model_field)](record_value)
