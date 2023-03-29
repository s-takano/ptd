from typing import Dict, List, Tuple, TypedDict, Union

class DataImporterConfig(TypedDict):
    target_name: str
    field_map: Dict[str, Union[str, Tuple[str, str]]]

IMPORT_CONFIGS: List[DataImporterConfig] = [
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