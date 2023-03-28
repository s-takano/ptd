from decimal import Decimal
import json
from sales_management import models
from django.db import models as django_models
import os
from sales_management.IMPORT_CONFIGS import IMPORT_CONFIGS
from sales_management.utils import parse_datetime

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
            except FileNotFoundError:
                raise Exception(f"file not found:{data_file_path}")
            except json.JSONDecodeError as json_error:
                raise Exception(f"json decode error:{json_error}")

        self.import_data(data)

    def import_data(self, data):
        identity_map = {}

        import_configs = [(config["target_name"], config)
                          for config in IMPORT_CONFIGS]
        try:
            for target_name, import_config in import_configs:
                pk_map = {}
                if target_name in data:
                    src_pk = self._find_src_pk(import_config)
                    model = getattr(models, import_config["target_name"])
                    pk_map = self._import_records(
                        data[target_name], import_config, src_pk, identity_map, model)

                identity_map[target_name] = pk_map

        except Exception as e:
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

    def _import_records(self, records, import_config, src_pk, identity_map, model):
        pk_map = {}

        for src in records:
            params = {model_field_name: self._get_dst_value(src, src_field, model, model_field_name, identity_map)
                      for model_field_name, src_field in import_config["field_map"].items()
                      if model_field_name != "pk"}

            s = model.objects.create(**params)
            if src_pk != "":
                pk_map[src[src_pk]] = s.pk

        return pk_map

    def _get_dst_value(self, src, src_field, model, model_field_name, identity_map):
        src_value = self._src_value(src, src_field, identity_map)
        field = self._field(model, model_field_name)
        return self._dst_value(src_value, field)

    def _find_src_pk(self, import_config):
        return next((src_field
                     for dst_field, src_field in import_config["field_map"].items()
                     if dst_field == "pk"), "")

    def _field(self, model, model_field_name):
        attr = getattr(model, model_field_name)
        field = attr.field
        return field

    def _src_value(self, src, src_field, identity_map):
        if isinstance(src_field, tuple):
            # if src_field is foreign key, return object if exists
            if src_field[0].startswith("[") and src_field[0].endswith("]"):
                model_name = src_field[0][1:-1]
                src_field_name = src_field[1]

                if src[src_field_name] not in identity_map[model_name]:
                    return None

                id = identity_map[model_name][src[src_field_name]]
                model = getattr(models, model_name)
                return model.objects.get(id=id)

            # if src_field is tuple and return tuple of values
            return tuple([src[f] for f in src_field])
        return src[src_field]

    def _dst_value(self, value, field):
        value_converters = {
            django_models.CharField: lambda x: x if x != "" else "",
            django_models.IntegerField: lambda x: int(x) if x != "" else 0,
            django_models.DecimalField: lambda x: Decimal(x) if x != "" else Decimal(0),
            django_models.DateField: lambda x: parse_datetime(x),
            django_models.DateTimeField: lambda x: parse_datetime(x) if not isinstance(x, tuple) else parse_datetime(*x),
            django_models.BooleanField: lambda x: True if x == "1" or x.upper() == "TRUE" else False,
            django_models.ForeignKey: lambda x: x,
            django_models.BigIntegerField: lambda x: int(x) if x != "" else 0,
        }
        return value_converters[type(field)](value)
