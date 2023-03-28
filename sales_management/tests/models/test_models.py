from datetime import datetime, timedelta, timezone
from decimal import Decimal
import json
import os
import pytest
from django.test import TestCase
from django.utils import timezone
from sales_management.models import Sales, SalesDetails, Seller, SalonItems, Emoney, EmoneyType, FreeeDeals, Hp, Omron, Payments, RetailItems
from django.utils.dateparse import parse_datetime


class TestModels(TestCase):
    def load_test_data(self):

        current_path = os.path.dirname(os.path.abspath(__file__))

        seller_map = {}
        try:
            with open(os.path.join(current_path, "..\\data\\seller.json")) as f_seller:
                self.test_data_seller = json.load(f_seller)
                for seller in self.test_data_seller:
                    s = Seller.objects.create(seller_name=seller["SallerName"])
                    seller_map[seller["ID"]] = s.id
        except Exception as e:
            raise Exception(f"import error:{'seller'}\n{e}")

        try:
            with open(os.path.join(current_path, "..\\data\\omron.json"), encoding="UTF-8") as f_omron:
                self.test_data_omron = json.load(f_omron)
                for omron in self.test_data_omron:
                    Omron.objects.create(
                        handling_date=self.parse_datetime(omron["お取扱日"]),
                        credit_company_code=omron["クレジット会社コード"],
                        credit_company_name=omron["クレジット会社名"],
                        payment_category=omron["支払区分"],
                        payment_name=omron["支払名称"],
                        installment_count_gift_value=omron["分割回数／ギフト券額面"],
                        gift_ticket_quantity=omron["ギフト券枚数"] if omron["ギフト券枚数"] != "" else None,
                        slip_number=omron["伝票番号"],
                        sales_amount=omron["売上金額"],
                        scheduled_payment_date1=self.parse_datetime(
                            omron["入金予定日１"]) if omron["入金予定日１"] != "" else None,
                        scheduled_payment_date2=self.parse_datetime(
                            omron["入金予定日２"]) if omron["入金予定日２"] != "" else None,
                    )
        except Exception as e:
            raise Exception(f"import error:{'omron'}\n{e}")

        try:
            sales_map = {}
            with open(os.path.join(current_path, "..\\data\\sales.json"), encoding="UTF-8") as f_sales:
                self.test_data_sales = json.load(f_sales)
                for sales in self.test_data_sales:
                    from_time = timezone.make_aware(
                            datetime.combine(datetime.strptime(sales["SalesDate"], "%Y/%m/%d").date(),
                                             datetime.strptime(sales["From"], "%H:%M:%S").time()))
               
                    to_time = timezone.make_aware(
                            datetime.combine(datetime.strptime(sales["SalesDate"], "%Y/%m/%d").date(),
                                             datetime.strptime(sales["To"], "%H:%M:%S").time()))
                 
                    o = Sales.objects.create(
                        code=sales["SalesId"],
                        customer=sales["Customer"],
                        from_time=from_time,
                        to_time=to_time,
                        gross_salon_sales=sales["GrossSalonSales"],
                        gross_retail_sales=sales["GrossRetailSales"],
                        total_gross_sales=sales["TotalGrossSales"],
                        total_salon_discount=sales["TotalSalonDiscount"],
                        retail_discount=sales["RetailDiscount"],
                        service_net_sales=sales["ServiceNetSales"],
                        retail_net_sales=sales["RetailNetSales"],
                        total_net_sales=sales["TotalNetSales"],
                        cash=sales["Cash"] if sales["Cash"] != "" else 0,
                        card_type=sales["CardType"],
                        card=sales["Card"] if sales["Card"] != "" else 0,
                        em=sales["EM"] if sales["EM"] != "" else 0,
                        prepaid=sales["Prepaid"] if sales["Prepaid"] != "" else 0,
                        credit=sales["Credit"] if sales["Credit"] != "" else 0,
                        tax=sales["Tax"] if sales["Tax"] != "" else 0,
                        comment=sales["Comment"],
                    )
                    sales_map[sales["Id"]] = o.id
        except Exception as e:
            raise Exception(f"import error:{'sales'}\n{e}")

        salon_item_map = {}
        try:
            with open(os.path.join(current_path, "..\\data\\salonitems.json"), encoding="UTF-8") as f_salon_items:
                self.test_data_salon_items = json.load(f_salon_items)
                for salon_item in self.test_data_salon_items:
                    d = salon_item["登録日付"]
                    o = SalonItems.objects.create(
                        category=salon_item["Category"],
                        number=salon_item["No"] if salon_item["No"] != "" else None,
                        display_name=salon_item["DisplayName"],
                        norm_name=salon_item["NormName"],
                        price=salon_item["Price"] if salon_item["Price"] != "" else None,
                        tax_category=salon_item["消費税区分"],
                        active=salon_item["Active"],
                        registration_date=self.parse_datetime(d),
                        update_date=self.parse_datetime(salon_item["更新日付"])
                    )
                    salon_item_map[salon_item["ID"]] = o.id
        except Exception as e:
            raise Exception(f"import error:{'salonitems'}\n{e}")

        retail_item_map = {}
        try:
            with open(os.path.join(current_path, "..\\data\\retailitems.json"), encoding="UTF-8") as f_retail_items:
                content = f_retail_items.read()
                content = content.replace('\\', '\\\\')
                self.test_data_retail_items = json.loads(content)
                for retail_item in self.test_data_retail_items:
                    o = RetailItems.objects.create(
                        category=retail_item["Category"],
                        number=retail_item["No"] if retail_item["No"] != "" else None,
                        display_name=retail_item["DisplayName"],
                        norm_name=retail_item["NormName"],
                        price=retail_item["Price"] if retail_item["Price"] != "" else None,
                        cost=retail_item["Cost"] if retail_item["Cost"] != "" else None,
                        vat_type=retail_item["VATType"],
                        vat_rate=retail_item["VATRate"] if retail_item["VATRate"] != "" else None,
                        product_category=retail_item["商品区分"],
                        supplier_name=retail_item["仕入先名"],
                        seller=Seller.objects.get(
                            id=seller_map[retail_item["Seller"]]),
                        active=retail_item["Active"],
                        registration_date=self.parse_datetime(
                            retail_item["RegistrationDate"]),
                        update_date=self.parse_datetime(
                            retail_item["UpdateDate"])
                    )
                    retail_item_map[retail_item["ID"]] = o.id
        except Exception as e:
            raise Exception(f"import error:{'retailitems'}\n{e}")

        try:
            with open(os.path.join(current_path, "..\\data\\salesdetails.json"), encoding="UTF-8") as f_sales_detail:
                self.test_data_sales_detail = json.load(f_sales_detail)
                for sales_detail in self.test_data_sales_detail:
                    if sales_detail["SaleId"] in sales_map:
                        SalesDetails.objects.create(
                            sale=Sales.objects.get(
                                id=sales_map[sales_detail["SaleId"]]),
                            payment=Sales.objects.get(
                                id=sales_map[sales_detail["PaymentId"]]),
                            customer=sales_detail["Customer"],
                            item_type="Salon Item" if sales_detail["ItemType"] == "技術" else "Retail Item",
                            salon_item=SalonItems.objects.get(
                                id=salon_item_map[sales_detail["ItemId"]]) if sales_detail["ItemType"] == "技術" else None,
                            retail_item=RetailItems.objects.get(
                                id=retail_item_map[sales_detail["ItemId"]]) if sales_detail["ItemType"] == "商品" else None,
                            staff=sales_detail["Staff"],
                            amount=sales_detail["Amount"],
                            gross_sales=sales_detail["Gross Sales"],
                            discount_type=sales_detail["Discount Type"],
                            discount=sales_detail["Discount"],
                            net_sales=sales_detail["Net Sales"],
                            field1=sales_detail["フィールド1"],
                            field2=sales_detail["フィールド2"],
                        )
        except Exception as e:
            raise Exception(f"import error:{'sales_detail'}\n{e}")

        try:
            with open(os.path.join(current_path, "..\\data\\payments.json"), encoding="UTF-8") as f_payments:
                content = f_payments.read()
                content = content.replace('\\', '\\\\')
                self.test_data_payments = json.loads(content)
                for payment in self.test_data_payments:
                    Payments.objects.create(
                        payment_id=payment["Payment ID"],
                        sale=Sales.objects.get(
                            id=sales_map[payment["SalesId"]]),
                        time=timezone.make_aware(datetime.combine(
                            datetime.strptime(
                                payment["Date"], "%Y/%m/%d").date(),
                            datetime.strptime(payment["Time"], "%H:%M:%S").time())),
                        total_collected=payment["Total Collected"],
                        fees=payment["Fees"],
                        net_total=payment["Net Total"],
                        customer_name=payment["Customer Name"],
                        card_brand=payment["Card Brand"],
                        pan_suffix=payment["PAN Suffix"],
                        deposit_date=timezone.make_aware(
                            datetime.strptime(payment["Deposit Date"], "%Y-%m-%d")) if payment["Deposit Date"] != "" else None,
                        fee_percentage_rate=payment["Fee Percentage Rate"],
                        field1=payment["フィールド1"],
                    )
        except Exception as e:
            raise Exception(f"import error:{'payments'}\n{e}")

        emoney_type_map = {}
        try:
            with open(os.path.join(current_path, "..\\data\\emtype.json"), encoding="UTF-8") as f_emoney_type:
                self.test_data_emoney_type = json.load(f_emoney_type)
                for emoney_type in self.test_data_emoney_type:
                    t = EmoneyType.objects.create(
                        partner=emoney_type["取引先"],
                        item=emoney_type["品目"],
                        type_name=emoney_type["TypeName"]
                    )
                    emoney_type_map[emoney_type["ID"]] = t.id
        except Exception as e:
            raise Exception(f"import error:{'emtype'}\n{e}")

        try:
            with open(os.path.join(current_path, "..\\data\\e-money.json"), encoding="UTF-8") as f_emoney:
                self.test_data_emoney = json.load(f_emoney)
                for emoney in self.test_data_emoney:
                    Emoney.objects.create(
                        type=EmoneyType.objects.get(
                            id=emoney_type_map[emoney["TypeId"]]) if emoney["TypeId"] != "" else None,
                        sale=Sales.objects.get(
                            id=sales_map[emoney["SalesId"]]) if emoney["SalesId"] != "" else None,
                        usage_date=self.parse_datetime(emoney["利用日付"]),
                        customer_name=emoney["顧客名"],
                        amount=emoney["利用金額"],
                        cashier=emoney["レジ担当"],
                    )
        except Exception as e:
            raise Exception(f"import error:{'e-money'}\n{e}")

        try:
            with open(os.path.join(current_path, "..\\data\\hp.json"), encoding="UTF-8") as f_hp:
                self.test_data_hp = json.load(f_hp)
                for hp in self.test_data_hp:
                    Hp.objects.create(
                        sale=Sales.objects.get(
                            id=sales_map[hp["SalesId"]]) if hp["SalesId"] != "" else None,
                        sales_date=self.parse_datetime(hp["SalesDate"]),
                        net_sales=hp["NetSales"] if hp["NetSales"] != "" else None,
                        points=hp["Points"] if hp["Points"] != "" else None,
                    )
        except Exception as e:
            raise Exception(f"import error:{'hp'}\n{e}")

        try:
            with open(os.path.join(current_path, "..\\data\\freeedeals.json"), encoding="UTF-8") as f_freee_deals:
                self.test_data_freee_deals = json.load(f_freee_deals)
                for freee_deals in self.test_data_freee_deals:
                    FreeeDeals.objects.create(
                        type=freee_deals["種別"],
                        number=freee_deals["No"],
                        title=freee_deals["表題行"],
                        date=self.parse_datetime(freee_deals["日付"]),
                        slip_number=freee_deals["伝票番号"],
                        debit_account=freee_deals["借方勘定科目"],
                        debit_sub_account=freee_deals["借方補助科目"],
                        debit_partner=freee_deals["借方取引先"],
                        debit_department=freee_deals["借方部門"],
                        debit_item=freee_deals["借方品目"],
                        debit_memo_tag=freee_deals["借方メモタグ"],
                        debit_tax_category=freee_deals["借方税区分"],
                        debit_amount=freee_deals["借方金額"] if freee_deals["借方金額"] != "" else None,
                        debit_tax_amount=freee_deals["借方税額"] if freee_deals["借方税額"] != "" else None,
                        credit_account=freee_deals["貸方勘定科目"],
                        credit_sub_account=freee_deals["貸方補助科目"],
                        credit_partner=freee_deals["貸方取引先"],
                        credit_department=freee_deals["貸方部門"],
                        credit_item=freee_deals["貸方品目"],
                        credit_memo_tag=freee_deals["貸方メモタグ"],
                        credit_tax_category=freee_deals["貸方税区分"],
                        credit_amount=freee_deals["貸方金額"] if freee_deals["貸方金額"] != "" else None,
                        credit_tax_amount=freee_deals["貸方税額"] if freee_deals["貸方税額"] != "" else None,
                        summary=freee_deals["摘要"],
                    )
        except Exception as e:
            raise Exception(f"import error:{'freeedeals'}\n{e}")

    def parse_datetime(self, date_string):
        if date_string == "":
            return None
        return timezone.make_aware(datetime.strptime(date_string, "%Y/%m/%d %H:%M:%S" if len(date_string) > 10 else "%Y/%m/%d"))

    def setUp(self):
        self.seller = Seller.objects.create(
            seller_name="Seller Name"
        )
        self.load_test_data()

    def test_sales(self):
        sales = Sales.objects.get(code="S202207080013")
        self.assertIsNotNone(sales.id)
        assert sales.customer == "C202207080013"
        assert sales.from_time == timezone.make_aware(
            datetime(2022, 7, 8, 12, 17))
        assert sales.to_time == timezone.make_aware(
            datetime(2022, 7, 8, 12, 18))
        assert sales.gross_salon_sales == Decimal("4400")
        assert sales.gross_retail_sales == Decimal("22000")
        assert sales.total_gross_sales == Decimal("26400")
        assert sales.total_salon_discount == Decimal("0")
        assert sales.retail_discount == Decimal("0")
        assert sales.service_net_sales == Decimal("4400")
        assert sales.retail_net_sales == Decimal("22000")
        assert sales.total_net_sales == Decimal("26400")
        assert sales.cash == Decimal("0")
        assert sales.card == Decimal("23400")
        assert sales.card_type == "[クレジット]"
        assert sales.em == Decimal("3000")
        assert sales.prepaid == Decimal("0")
        assert sales.credit == Decimal("0")
        assert sales.tax == Decimal("2400")
        assert sales.comment == "Comment"

    def test_sales_details(self):
        sales = Sales.objects.get(code="S202207080013")
        sales_detail_retail = sales.details.filter(
            item_type="Retail Item").first()

        assert sales_detail_retail.sale == sales
        assert sales_detail_retail.payment == sales
        assert sales_detail_retail.customer == "Customer_56427"
        assert sales_detail_retail.item_type == "Retail Item"
        assert sales_detail_retail.staff == "Staff_56427"
        assert sales_detail_retail.amount == 1
        assert sales_detail_retail.gross_sales == Decimal("22000")
        assert sales_detail_retail.discount_type == ""
        assert sales_detail_retail.discount == Decimal("0")
        assert sales_detail_retail.net_sales == Decimal("22000")
        assert sales_detail_retail.field1 == "フィールド1"
        assert sales_detail_retail.field2 == "フィールド2"
        assert sales_detail_retail.retail_item.category == "Category_37841"
        assert sales_detail_retail.retail_item.number == 4
        assert sales_detail_retail.retail_item.display_name == "DisplayName_37841"
        assert sales_detail_retail.retail_item.norm_name == "NormName_37841"
        assert sales_detail_retail.retail_item.price == Decimal("22000")
        assert sales_detail_retail.retail_item.cost == Decimal("0")
        assert sales_detail_retail.retail_item.vat_type == "内税"
        assert sales_detail_retail.retail_item.vat_rate == Decimal("10")
        assert sales_detail_retail.retail_item.product_category == "両用"
        assert sales_detail_retail.retail_item.supplier_name == "仕入先名_37841"
        assert sales_detail_retail.retail_item.seller.seller_name == "A"
        assert sales_detail_retail.retail_item.active == True
        assert sales_detail_retail.retail_item.registration_date \
            == timezone.make_aware(datetime(2018, 12, 12, 12, 33, 43))
        assert sales_detail_retail.retail_item.update_date \
            == timezone.make_aware(datetime(2018, 12, 12, 12, 33, 43))

        # test only difference between retail and salon
        sales_detail_salon = sales.details.filter(
            item_type="Salon Item").first()
        assert sales_detail_salon.item_type == "Salon Item"
        assert sales_detail_salon.salon_item.category == "Category_9031"
        assert sales_detail_salon.salon_item.number == 9
        assert sales_detail_salon.salon_item.display_name == "DisplayName_9031"
        assert sales_detail_salon.salon_item.norm_name == "NormName_9031"
        assert sales_detail_salon.salon_item.price == Decimal("4400")
        assert sales_detail_salon.salon_item.tax_category == "内税"
        assert sales_detail_salon.salon_item.active == True
        assert sales_detail_salon.salon_item.registration_date \
            == timezone.make_aware(datetime(2010, 2, 12, 15, 41, 28))
        assert sales_detail_salon.salon_item.update_date \
            == timezone.make_aware(datetime(2022, 2, 13, 10, 9, 30))

    def test_payment_details(self):
        payment_sales =  Sales.objects.get(code="S202207180006")
        sale_sales = Sales.objects.get(code="S202207180007")

        assert payment_sales.details.first().payment == payment_sales
        assert sale_sales.details.first().payment == payment_sales
        assert sale_sales.details.first().sale == sale_sales

        assert payment_sales.details.count()==2
        assert sale_sales.details.count() == 2

        assert payment_sales.payment_details.count() == 4
        assert sale_sales.payment_details.count() == 0



    def test_emoney(self):
        sales = Sales.objects.get(code="S202207040012")
        emoney = sales.emoney.first()
        emoney_type = emoney.type

        assert emoney_type.partner == "P7"
        assert emoney_type.item == "HP"
        assert emoney_type.type_name == "HP(値引)"

        self.assertIsNotNone(emoney.id)
        assert emoney.sale == sales
        assert emoney.usage_date == timezone.make_aware(datetime(2022, 7, 4))
        assert emoney.customer_name == "C1"
        assert emoney.amount == 1000
        assert emoney.cashier == "M"

    def test_freee_deals(self):
        freee_deal = FreeeDeals.objects.get(number=43881)
        self.assertIsNotNone(freee_deal.id)
        assert freee_deal.type == "会計"
        assert freee_deal.number == 43881
        assert freee_deal.title == "[明細行]"
        assert freee_deal.date == \
            timezone.make_aware(datetime(2022, 12, 15))
        assert freee_deal.slip_number == 2
        assert freee_deal.debit_account == "銀行"
        assert freee_deal.debit_sub_account == ""
        assert freee_deal.debit_partner == ""
        assert freee_deal.debit_department == ""
        assert freee_deal.debit_item == ""
        assert freee_deal.debit_memo_tag == ""
        assert freee_deal.debit_tax_category == "対象外"
        assert freee_deal.debit_amount == Decimal("1596")
        assert freee_deal.debit_tax_amount == None
        assert freee_deal.credit_account == "売掛金"
        assert freee_deal.credit_sub_account == ""
        assert freee_deal.credit_partner == "顧客(掛売)"
        assert freee_deal.credit_department == ""
        assert freee_deal.credit_item == ""
        assert freee_deal.credit_memo_tag == ""
        assert freee_deal.credit_tax_category == "対象外"
        assert freee_deal.credit_amount == Decimal("1650")
        assert freee_deal.credit_tax_amount == None
        assert freee_deal.summary == "掛売(2022/07/16)"

    def test_hp(self):
        sale = Sales.objects.get(code="S202207040012")
        hp = sale.hp.first()
        assert hp.sales_date == timezone.make_aware(datetime(2022, 7, 4))
        assert hp.net_sales == 9800
        assert hp.points == 100.00

    def test_omron(self):
        omron = Omron.objects.get(slip_number="194")
        self.assertIsNotNone(omron.id)
        assert omron.handling_date == timezone.make_aware(
            datetime(2022, 7, 6))
        assert omron.credit_company_code == "888"
        assert omron.credit_company_name == "ﾎﾟｲﾝﾄｸｰﾎﾟﾝ"
        assert omron.payment_category == "10"
        assert omron.payment_name == "一括"
        assert omron.installment_count_gift_value == 1
        assert omron.gift_ticket_quantity == 1
        assert omron.slip_number == "194"
        assert omron.sales_amount == Decimal("10000")
        assert omron.scheduled_payment_date1 == \
            timezone.make_aware(datetime(2022, 7, 20))
        assert omron.scheduled_payment_date2 == \
            timezone.make_aware(datetime(2022, 7, 21))

    def test_payments(self):
        sale = Sales.objects.get(code="S202207040012")
        payment = sale.payments.first()
        self.assertIsNotNone(payment.id)
        assert payment.payment_id == "PaymentID_15204"
        assert payment.sale == sale
        assert payment.time == \
            timezone.make_aware(datetime(2022, 7, 4, 15, 40, 13))
        assert payment.total_collected == Decimal("8800")
        assert payment.fees == Decimal("-286")
        assert payment.net_total == Decimal("8514")
        assert payment.customer_name == "Customer1"
        assert payment.card_brand == "SOX"
        assert payment.pan_suffix == "6234"
        assert payment.deposit_date == \
            timezone.make_aware(datetime(2022, 7, 7))
        assert payment.fee_percentage_rate == Decimal("3.25")
        assert payment.field1 == "フィールド1"
