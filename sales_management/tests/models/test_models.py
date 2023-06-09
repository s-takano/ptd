from datetime import datetime, timezone
from decimal import Decimal
import os
from django.utils import timezone
import pytest
from sales_management.data_importer import DataImporter
from sales_management.models import Emoney, HPs, Payments, RetailItems, Sales, SalesItems, SalonItems, Sellers, FreeeDeals, OmronTransactions
from django.db.models import ProtectedError

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
def test_sales_get(import_test_data: None):
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


@pytest.mark.django_db()
def test_sales_delete(import_test_data: None):
    sales = Sales.objects.get(code="S202207080013")
    emoney_id = sales.emoney.first().id
    payment_id = sales.payments.first().id
    hp_id = sales.hps.first().id
    total_item_count = SalesItems.objects.count()
    item_count = sales.items.count()

    sales.delete()

    with pytest.raises(Sales.DoesNotExist):
        Sales.objects.get(code="S202207080013")
    # Delete should cascade to SalesItems
    assert SalesItems.objects.count() == total_item_count - item_count
    # Delete should set NULL to Emoney
    assert Emoney.objects.get(id=emoney_id).sale is None
    # Delete should set NULL to Payments
    assert Payments.objects.get(id=payment_id).sale is None
    # Delete should set NULL to Hps
    assert HPs.objects.get(id=hp_id).sale is None
    

@pytest.mark.django_db
def test_sales_items_get(import_test_data: None):
    sales = Sales.objects.get(code="S202207080013")
    sales_detail_retail = sales.items.filter(
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
    assert sales_detail_retail.retail_item.vat_category == "内税"
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
    sales_detail_salon = sales.items.filter(
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
def test_sales_items_delete(import_test_data: None):
    sales_items = SalesItems.objects.get(id=13)
    total_salon_item_count = SalonItems.objects.count()
    total_retail_item_count = RetailItems.objects.count()
    total_seller_count = Sellers.objects.count()

    sales_items.delete()
    with pytest.raises(SalesItems.DoesNotExist):
        SalesItems.objects.get(id=13)
    
    # SalonItems should not be deleted when Sales is deleted
    assert SalonItems.objects.count() == total_salon_item_count
    # RetailItems should not be deleted when Sales is deleted
    assert RetailItems.objects.count() == total_retail_item_count
    # Delete should not cascade to Sellers
    assert Sellers.objects.count() == total_seller_count



@pytest.mark.django_db
def test_payment_items(import_test_data: None):
    payment_sales = Sales.objects.get(code="S202207180006")
    sale_sales = Sales.objects.get(code="S202207180007")

    assert payment_sales.items.first().payment == payment_sales
    assert sale_sales.items.first().payment == payment_sales
    assert sale_sales.items.first().sale == sale_sales

    assert payment_sales.items.count() == 2
    assert sale_sales.items.count() == 2

    assert payment_sales.payment_items.count() == 4
    assert sale_sales.payment_items.count() == 0

@pytest.mark.django_db
def test_emoney_get(import_test_data: None):
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
def test_freee_deals_get(import_test_data: None):
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
def test_hp_get(import_test_data: None):
    sale = Sales.objects.get(code="S202207040012")
    hps = sale.hps.first()
    assert hps.sales_date == timezone.make_aware(datetime(2022, 7, 4))
    assert hps.net_sales == 9800
    assert hps.points == 100.00

@pytest.mark.django_db
def test_omron_get(import_test_data: None):
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
def test_payments_get(import_test_data: None):
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

@pytest.mark.django_db
def test_salon_items_get(import_test_data: None):
    salon_item = SalonItems.objects.get(id=1)
    assert salon_item.id is not None
    assert salon_item.category == "Category_8747"
    assert salon_item.number == int("6")
    assert salon_item.display_name == "DisplayName_8747"
    assert salon_item.norm_name == "NormName_8747"
    assert salon_item.price == Decimal("0")
    assert salon_item.tax_category == "内税"
    assert salon_item.active == bool("True")
    assert salon_item.registration_date == \
        timezone.make_aware(datetime(2007, 12, 20, 15, 5, 10))
    assert salon_item.update_date == \
        timezone.make_aware(datetime(2012, 6, 25, 15, 3, 58))

@pytest.mark.django_db
def test_salon_items_delete_used(import_test_data: None):
    # initial_count = SalonItems.objects.count()
    salon_item = SalonItems.objects.get(id=1)

    # used salon_item cannot be deleted
    with pytest.raises(ProtectedError):
        salon_item.delete()

@pytest.mark.django_db
def test_salon_items_delete_unused(import_test_data: None):
    initial_count = SalonItems.objects.count()

    # unused salon_item can be deleted
    salon_item = SalonItems.objects.get(id=1)
    salon_item.sales_items.all().delete()
    salon_item.delete()

    assert SalonItems.objects.count() == initial_count - 1

@pytest.mark.django_db
def test_retail_items_get(import_test_data: None):
    retail_item = RetailItems.objects.get(display_name = "DisplayName_37841")
    assert retail_item.id is not None
    assert retail_item.category == "Category_37841"
    assert retail_item.number == int("4")
    assert retail_item.display_name == "DisplayName_37841"
    assert retail_item.norm_name == "NormName_37841"
    assert retail_item.price == Decimal("22000")
    assert retail_item.cost == Decimal("0")
    assert retail_item.vat_category == "内税"
    assert retail_item.vat_rate == Decimal("10")
    assert retail_item.product_category == "両用"
    assert retail_item.supplier_name == "仕入先名_37841"
    assert retail_item.seller.id == 1
    assert retail_item.active == bool("True")
    assert retail_item.registration_date == \
        timezone.make_aware(datetime(2018, 12, 12, 12, 33, 43))
    assert retail_item.update_date == \
        timezone.make_aware(datetime(2018, 12, 12, 12, 33, 43))

@pytest.mark.django_db
def test_retail_items_delete_used(import_test_data: None):
    retail_item = RetailItems.objects.get(id=1)

    # used retail_item cannot be deleted
    with pytest.raises(ProtectedError):
        retail_item.delete()

@pytest.mark.django_db
def test_retail_items_delete_unused(import_test_data: None):
    initial_count = RetailItems.objects.count()

    # unused retail_item can be deleted
    retail_item = RetailItems.objects.get(id=1)
    retail_item.sales_items.all().delete()
    retail_item.delete()

    assert RetailItems.objects.count() == initial_count - 1