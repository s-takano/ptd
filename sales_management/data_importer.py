from decimal import Decimal
import json
import logging
from sales_management import models
from django.db import models as django_models
import os
from sales_management.IMPORT_CONFIGS import IMPORT_CONFIGS
from sales_management.utils import parse_datetime

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


class DataImporter():
    def import_data_file(self, path):
        data_files = self._search_data_files(path)

        data = {}
        for target_name, data_file_path in data_files:
            try:
                with open(data_file_path, encoding="UTF-8") as f:
                    content = f.read()
                    content = content.replace('\\', '\\\\')
                    data[target_name] = json.loads(content)
            except FileNotFoundError as file_not_found_error:
                logger.error(file_not_found_error)
                raise Exception(f"file not found:{data_file_path}")
            except json.JSONDecodeError as json_error:
                logger.error(json_error)
                raise Exception(f"json decode error:{json_error}")

        self.import_data(data)

    def import_data(self, data):
        identity_map = {}

        try:
            for config in IMPORT_CONFIGS:
                target_name = config["target_name"]
                pk_map = {}
                if target_name in data:
                    src_pk = self._find_data_record_pk(config)
                    model = getattr(models, target_name)
                    pk_map = self._import_records(
                        data[target_name], config, src_pk, identity_map, model)

                identity_map[target_name] = pk_map

        except Exception as e:
            logger.error(e)
            raise Exception(f"import error:{e}")

    def _search_data_files(self, path):
        # enum all file names in `path`
        data_file_names = [os.path.splitext(file_name)[0].lower()
                           for file_name in os.listdir(path)
                           if os.path.splitext(file_name)[1] == ".json"]

        data_file_paths = []
        # load data files in the order of `import_configs`
        for config in IMPORT_CONFIGS:
            if config["target_name"].lower() in data_file_names:
                data_file_path = os.path.join(
                    path, config["target_name"] + ".json")
                data_file_paths.append((config["target_name"], data_file_path))

        return data_file_paths

    def _import_records(self, records, config, data_record_pk, identity_map, model):
        pk_map = {}

        for data_record in records:
            params = {model_field_name: self._get_model_value(data_record, data_field_name, model, model_field_name, identity_map)
                      for model_field_name, data_field_name in config["field_map"].items()
                      if model_field_name != "pk"}

            s = model.objects.create(**params)
            if data_record_pk != "":
                pk_map[data_record[data_record_pk]] = s.pk

        return pk_map

    def _get_model_value(self, data_record, data_field_name, model, model_field_name, identity_map):
        data_value = self._src_value(
            data_record, data_field_name, identity_map)
        model_field = self._model_field(model, model_field_name)
        return self._convert_value(data_value, model_field)

    def _find_data_record_pk(self, config):
        return next((src_field
                     for dst_field, src_field in config["field_map"].items()
                     if dst_field == "pk"), "")

    def _model_field(self, model, model_field_name):
        attr = getattr(model, model_field_name)
        field = attr.field
        return field

    def _src_value(self, data_record, data_field_name, identity_map):
        if isinstance(data_field_name, tuple):
            # if src_field is foreign key, return object if exists
            if data_field_name[0].startswith("[") and data_field_name[0].endswith("]"):
                model_name = data_field_name[0][1:-1]
                id_field_name = data_field_name[1]

                if data_record[id_field_name] not in identity_map[model_name]:
                    return None

                id = identity_map[model_name][data_record[id_field_name]]
                model = getattr(models, model_name)
                return model.objects.get(id=id)

            # if src_field is tuple and return tuple of values
            return tuple([data_record[f] for f in data_field_name])
        return data_record[data_field_name]

    def _convert_value(self, data_value, model_field):
        value_converters = {
            django_models.CharField: lambda x: x if x != "" else "",
            django_models.IntegerField: lambda x: int(x) if x != "" else 0,
            django_models.DecimalField: lambda x: Decimal(x) if x != "" else Decimal(0),
            django_models.DateField: parse_datetime,
            django_models.DateTimeField: lambda x: parse_datetime(x) if not isinstance(x, tuple) else parse_datetime(*x),
            django_models.BooleanField: lambda x: True if x == "1" or x.upper() == "TRUE" else False,
            django_models.ForeignKey: lambda x: x,
            django_models.BigIntegerField: lambda x: int(x) if x != "" else 0,
        }
        return value_converters[type(model_field)](data_value)
