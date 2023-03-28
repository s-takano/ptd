from decimal import Decimal
import json
from sales_management import models
from django.db import models as django_models
import os
from sales_management.utils import parse_datetime


class DataImporter():
    import_configs = [
        {
            "target_name": "Sellers",
            "field_map": {
                "pk": "ID",
                "seller_name": "SallerName"
            }
        },
        {
            "target_name": "OmronTransactions",
            "field_map": {
                "pk": "ID",
                "handling_date": "お取扱日",
                "credit_company_code": "クレジット会社コード",
                "credit_company_name": "クレジット会社名",
                "payment_category": "支払区分",
                "payment_name": "支払名称",
                "installment_count_gift_value": "分割回数／ギフト券額面",
                "gift_ticket_quantity": "ギフト券枚数",
                "slip_number": "伝票番号",
                "sales_amount": "売上金額",
                "scheduled_payment_date1": "入金予定日１",
                "scheduled_payment_date2": "入金予定日２"}
        },
        {
            "target_name": "Sales",
            "field_map": {
                "pk": "Id",
                "code": "SalesId",
                "customer": "Customer",
                "from_time": ("SalesDate", "From"),
                "to_time": ("SalesDate", "To"),
                "gross_salon_sales": "GrossSalonSales",
                "gross_retail_sales": "GrossRetailSales",
                "total_gross_sales": "TotalGrossSales",
                "total_salon_discount": "TotalSalonDiscount",
                "retail_discount": "RetailDiscount",
                "service_net_sales": "ServiceNetSales",
                "retail_net_sales": "RetailNetSales",
                "total_net_sales": "TotalNetSales",
                "cash": "Cash",
                "card_type": "CardType",
                "card": "Card",
                "em": "EM",
                "prepaid": "Prepaid",
                "credit": "Credit",
                "tax": "Tax",
                "comment": "Comment"
            }
        },
        {
            "target_name": "SalonItems",
            "field_map": {
                "pk": "ID",
                "category": "Category",
                "number": "No",
                "display_name": "DisplayName",
                "norm_name": "NormName",
                "price": "Price",
                "tax_category": "消費税区分",
                "active": "Active",
                "registration_date": "登録日付",
                "update_date": "更新日付"
            }
        },
        {
            "target_name": "RetailItems",
            "field_map": {
                "pk": "ID",
                "category": "Category",
                "number": "No",
                "display_name": "DisplayName",
                "norm_name": "NormName",
                "price": "Price",
                "cost": "Cost",
                "vat_type": "VATType",
                "vat_rate": "VATRate",
                "product_category": "商品区分",
                "supplier_name": "仕入先名",
                "seller": ("[Sellers]", "Seller"),
                "active": "Active",
                "registration_date": "RegistrationDate",
                "update_date": "UpdateDate"
            }
        },
        {
            "target_name": "SalesDetails",
            "field_map": {
                "pk": "ID",
                "sale": ("[Sales]", "SaleId"),
                "payment": ("[Sales]", "PaymentId"),
                "customer": "Customer",
                "item_type": "ItemType",
                "salon_item": ("[SalonItems]", "ItemId"),
                "retail_item": ("[RetailItems]", "ItemId"),
                "staff": "Staff",
                "amount": "Amount",
                "gross_sales": "Gross Sales",
                "discount_type": "Discount Type",
                "discount": "Discount",
                "net_sales": "Net Sales",
                "field1": "フィールド1",
                "field2": "フィールド2"
            }
        },
        {
            "target_name": "Payments",
            "field_map": {
                "payment_id": "Payment ID",
                "sale": ("[Sales]", "SalesId"),
                "time": ("Date", "Time"),
                "total_collected": "Total Collected",
                "fees": "Fees",
                "net_total": "Net Total",
                "customer_name": "Customer Name",
                "card_brand": "Card Brand",
                "pan_suffix": "PAN Suffix",
                "deposit_date": "Deposit Date",
                "fee_percentage_rate": "Fee Percentage Rate",
                "field1": "フィールド1"
            }
        },
        {
            "target_name": "EmoneyTypes",
            "field_map": {
                "pk": "ID",
                "partner": "取引先",
                "item": "品目",
                "type_name": "TypeName"
            }
        },
        {
            "target_name": "Emoney",
            "field_map": {
                "pk": "Id",
                "type": ("[EmoneyTypes]", "TypeId"),
                "sale": ("[Sales]", "SalesId"),
                "usage_date": "利用日付",
                "customer_name": "顧客名",
                "amount": "利用金額",
                "cashier": "レジ担当"
            }
        },
        {
            "target_name": "HPs",
            "field_map": {
                "pk": "ID",
                "sale": ("[Sales]", "SalesId"),
                "sales_date": "SalesDate",
                "net_sales": "NetSales",
                "points": "Points",
            }
        },
        {
            "target_name": "FreeeDeals",
            "field_map": {
                "type": "種別",
                "number": "No",
                "title": "表題行",
                "date": "日付",
                "slip_number": "伝票番号",
                "debit_account": "借方勘定科目",
                "debit_sub_account": "借方補助科目",
                "debit_partner": "借方取引先",
                "debit_department": "借方部門",
                "debit_item": "借方品目",
                "debit_memo_tag": "借方メモタグ",
                "debit_tax_category": "借方税区分",
                "debit_amount": "借方金額",
                "debit_tax_amount": "借方税額",
                "credit_account": "貸方勘定科目",
                "credit_sub_account": "貸方補助科目",
                "credit_partner": "貸方取引先",
                "credit_department": "貸方部門",
                "credit_item": "貸方品目",
                "credit_memo_tag": "貸方メモタグ",
                "credit_tax_category": "貸方税区分",
                "credit_amount": "貸方金額",
                "credit_tax_amount": "貸方税額",
                "summary": "摘要"
            }
        }
    ]

    def import_data_file(self, path):
        data_files = self._search_data_files(path)

        data = {}
        for target_name, data_file_path in data_files:
            with open(data_file_path, encoding="UTF-8") as f:
                content = f.read()
                content = content.replace('\\', '\\\\')
                data[target_name] = json.loads(content)

        self.import_data(data)

    def import_data(self, data):
        identity_map = {}

        import_configs = [(config["target_name"], config)
                          for config in DataImporter.import_configs]
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
        for config in DataImporter.import_configs:
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
