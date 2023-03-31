from datetime import datetime, timezone
from decimal import Decimal
import os
from django.utils import timezone
import pytest
from sales_management.data_importer import DataImporter
from sales_management.models import Sales, Sellers, FreeeDeals, OmronTransactions

@pytest.fixture()
def import_test_data(django_db_blocker, django_db_setup):
    current_path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_path, f"..\\data")
    with django_db_blocker.unblock():
        importer = DataImporter()
        importer.import_data_files(directory_path=path)
    yield
    importer.clean_up()


@pytest.mark.django_db
def test_sales(import_test_data):
    sales = Sales.objects.get(code="S202207080013")
    assert sales.id is not None
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

@pytest.mark.django_db
def test_sales_details(import_test_data):
    sales = Sales.objects.get(code="S202207080013")
    sales_detail_retail = sales.details.filter(
        item_type="商品").first()

    assert sales_detail_retail.sale == sales
    assert sales_detail_retail.payment == sales
    assert sales_detail_retail.customer == "Customer_56427"
    assert sales_detail_retail.item_type == "商品"
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
        item_type="技術").first()
    assert sales_detail_salon.item_type == "技術"
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

@pytest.mark.django_db
def test_payment_details(import_test_data):
    payment_sales = Sales.objects.get(code="S202207180006")
    sale_sales = Sales.objects.get(code="S202207180007")

    assert payment_sales.details.first().payment == payment_sales
    assert sale_sales.details.first().payment == payment_sales
    assert sale_sales.details.first().sale == sale_sales

    assert payment_sales.details.count() == 2
    assert sale_sales.details.count() == 2

    assert payment_sales.payment_details.count() == 4
    assert sale_sales.payment_details.count() == 0

@pytest.mark.django_db
def test_emoney(import_test_data):
    sales = Sales.objects.get(code="S202207040012")
    emoney = sales.emoney.first()
    emoney_type = emoney.type

    assert emoney_type.partner == "P7"
    assert emoney_type.item == "HP"
    assert emoney_type.type_name == "HP(値引)"

    assert emoney.id is not None
    assert emoney.sale == sales
    assert emoney.usage_date == timezone.make_aware(datetime(2022, 7, 4))
    assert emoney.customer_name == "C1"
    assert emoney.amount == 1000
    assert emoney.cashier == "M"

@pytest.mark.django_db
def test_freee_deals(import_test_data):
    freee_deal = FreeeDeals.objects.get(number=43881)
    assert freee_deal.id is not None
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
    assert freee_deal.debit_tax_amount == Decimal("0")
    assert freee_deal.credit_account == "売掛金"
    assert freee_deal.credit_sub_account == ""
    assert freee_deal.credit_partner == "顧客(掛売)"
    assert freee_deal.credit_department == ""
    assert freee_deal.credit_item == ""
    assert freee_deal.credit_memo_tag == ""
    assert freee_deal.credit_tax_category == "対象外"
    assert freee_deal.credit_amount == Decimal("1650")
    assert freee_deal.credit_tax_amount == Decimal("0")
    assert freee_deal.summary == "掛売(2022/07/16)"

@pytest.mark.django_db
def test_hp(import_test_data):
    sale = Sales.objects.get(code="S202207040012")
    hps = sale.hps.first()
    assert hps.sales_date == timezone.make_aware(datetime(2022, 7, 4))
    assert hps.net_sales == 9800
    assert hps.points == 100.00

@pytest.mark.django_db
def test_omron(import_test_data):
    omron = OmronTransactions.objects.get(slip_number="194")
    assert omron.id is not None
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

@pytest.mark.django_db
def test_payments(import_test_data):
    sale = Sales.objects.get(code="S202207040012")
    payment = sale.payments.first()
    assert payment.id is not None
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
