from datetime import datetime, timedelta, timezone
from decimal import Decimal
import pytest
from django.test import TestCase
from django.utils import timezone
from sales_management.models import Sales, SalesDetails, Seller, SalonItems, Emoney, EmoneyType, FreeeDeals, Hp, Omron, Payments, RetailItems


class TestModels(TestCase):
    def setUp(self):
        self.sales = Sales.objects.create(
            code="TestSales123",
            customer="John Doe",
            from_time="2022-03-22T10:30:00+09:00",  # Japanese time should be used
            to_time="2022-03-22T12:30:00+09:00",  # Japanese time should be used
            gross_salon_sales=100.00,
            gross_retail_sales=50.00,
            total_gross_sales=150.00,
            total_salon_discount=10.00,
            retail_discount=5.00,
            service_net_sales=90.00,
            retail_net_sales=45.00,
            total_net_sales=135.00,
            cash=80.00,
            card=55.00,
            card_type="Visa",
            em=10.00,
            prepaid=5.00,
            credit=10.00,
            tax=5.00,
            comment="Test comment"
        )

        self.seller = Seller.objects.create(
            seller_name="Seller Name"
        )

        self.salon_item = SalonItems.objects.create(
            category="Category",
            number=1,
            display_name="Display Name",
            norm_name="Norm Name",
            price=100.00,
            tax_category="Tax Category",
            active=True,
            registration_date=timezone.make_aware(
                datetime(2021, 3, 22, 10, 30)),
            update_date=timezone.make_aware(datetime(2021, 3, 22, 10, 30))
        )

        self.retail_item = RetailItems.objects.create(
            category="Electronics",
            number=1,
            display_name="Smartphone",
            norm_name="Smartphone",
            price=900.00,
            cost=600.00,
            vat_type="Standard",
            vat_rate=10.00,
            product_category="Phone",
            supplier_name="Phone Manufacturer",
            seller=self.seller,
            active=True,
            registration_date=timezone.make_aware(datetime(2022, 1, 1)),
            update_date=timezone.make_aware(datetime(2022, 2, 15)),
        )

        self.sales_detail_salon = SalesDetails.objects.create(
            sale=self.sales,
            payment=self.sales,
            customer="Customer Name",
            item_type="Salon Item",
            salon_item=self.salon_item,
            staff="Staff Name",
            amount=1,
            gross_sales=Decimal('100.00'),
            discount_type="Discount Type",
            discount=Decimal('10.00'),
            net_sales=Decimal('90.00'),
            field1="Field1 Value",
            field2="Field2 Value",
        )
        
        self.sales_detail_retail = SalesDetails.objects.create(
            sale=self.sales,
            payment=self.sales,
            customer="Customer Name",
            item_type="Retail Item",
            retail_item=self.retail_item,
            staff="Staff Name",
            amount=1,
            gross_sales=Decimal('100.00'),
            discount_type="Discount Type",
            discount=Decimal('10.00'),
            net_sales=Decimal('90.00'),
            field1="Field1 Value",
            field2="Field2 Value",
        )

        self.payment = Payments.objects.create(
            payment_id="PAY12345",
            sale=self.sales,
            date=timezone.make_aware(datetime(2022, 3, 22)),
            time=timezone.make_aware(datetime(2022, 3, 22, 10, 30)),
            total_collected=1500.00,
            fees=50.00,
            net_total=1450.00,
            customer_name="John Doe",
            card_brand="Visa",
            pan_suffix="1234",
            deposit_date="2022-03-23",
            fee_percentage_rate=3.00,
            field1="SampleField1",
        )

        
        self.emoney_type = EmoneyType.objects.create(
            partner="Partner",
            item="Item",
            type_name="Type Name"
        )

        self.emoney = Emoney.objects.create(
            type=self.emoney_type,
            sale=self.sales,
            usage_date=timezone.make_aware(datetime(2021, 3, 22, 10, 30)),
            customer_name="Customer Name",
            amount=100.00,
            cashier="Cashier",
        )

        self.freee_deals = FreeeDeals.objects.create(
            type="Example Type",
            number=12345,
            title="Example Title",
            date=timezone.make_aware(datetime(2022, 3, 22)),
            slip_number=12,
            debit_account="Example Debit Account",
            debit_sub_account="Example Debit Sub Account",
            debit_partner="Example Debit Partner",
            debit_department="Example Debit Department",
            debit_item="Example Debit Item",
            debit_memo_tag="Example Debit Memo Tag",
            debit_tax_category="Example Debit Tax Category",
            debit_amount=1000.00,
            debit_tax_amount=100.00,
            credit_account="Example Credit Account",
            credit_sub_account="Example Credit Sub Account",
            credit_partner="Example Credit Partner",
            credit_department="Example Credit Department",
            credit_item="Example Credit Item",
            credit_memo_tag="Example Credit Memo Tag",
            credit_tax_category="Example Credit Tax Category",
            credit_amount=1000.00,
            credit_tax_amount=100.00,
            summary="Example Summary",
        )

        self.hp = Hp.objects.create(
            sale=self.sales,
            sales_date=timezone.make_aware(datetime(2022, 3, 22)),
            net_sales=1000.00,
            points=200.00,
        )

        self.omron = Omron.objects.create(
            handling_date=timezone.make_aware(datetime(2022, 3, 22)),
            credit_company_code="12345",
            credit_company_name="CreditCompany",
            payment_category="PaymentCategory",
            payment_name="PaymentName",
            installment_count_gift_value=12,
            gift_ticket_quantity=5,
            slip_number="SL123456",
            sales_amount=1500.00,
            scheduled_payment_date1=timezone.make_aware(datetime(2022, 4, 22)),
            scheduled_payment_date2=timezone.make_aware(datetime(2022, 5, 22)),
        )



    def test_sales(self):
        sales = Sales.objects.get(code="TestSales123")
        self.assertIsNotNone(sales.id)
        assert sales.code == "TestSales123"
        assert sales.customer == "John Doe"
        assert sales.from_time == timezone.make_aware(
            datetime(2022, 3, 22, 10, 30))  # compare with Japanese time
        assert sales.to_time == timezone.make_aware(
            datetime(2022, 3, 22, 12, 30))  # compare with Japanese time
        assert sales.gross_salon_sales == 100.00
        assert sales.gross_retail_sales == 50.00
        assert sales.total_gross_sales == 150.00
        assert sales.total_salon_discount == 10.00
        assert sales.retail_discount == 5.00
        assert sales.service_net_sales == 90.00
        assert sales.retail_net_sales == 45.00
        assert sales.total_net_sales == 135.00
        assert sales.cash == 80.00
        assert sales.card == 55.00
        assert sales.card_type == "Visa"
        assert sales.em == 10.00
        assert sales.prepaid == 5.00
        assert sales.credit == 10.00
        assert sales.tax == 5.00
        assert sales.comment == "Test comment"


    def test_sales_details_salon(self):
        sales = Sales.objects.get(code="TestSales123")
        sales_detail = sales.sales_details_sale.filter(item_type="Salon Item").first()

        self.assertIsNotNone(sales_detail.id)
        assert sales_detail.sale_id == self.sales.id
        assert sales_detail.payment_id == self.sales.id
        assert sales_detail.customer == "Customer Name"
        assert sales_detail.item_type == "Salon Item"
        assert sales_detail.salon_item_id == self.salon_item.id
        assert sales_detail.staff == "Staff Name"
        assert sales_detail.amount == 1
        assert sales_detail.gross_sales == Decimal('100.00')
        assert sales_detail.discount_type == "Discount Type"
        assert sales_detail.discount == Decimal('10.00')
        assert sales_detail.net_sales == Decimal('90.00')
        assert sales_detail.field1 == "Field1 Value"
        assert sales_detail.field2 == "Field2 Value"


    def test_sales_details_retail(self):
        sales = Sales.objects.get(code="TestSales123")
        sales_detail = sales.sales_details_sale.filter(item_type="Retail Item").first()

        self.assertIsNotNone(sales_detail.id)
        assert sales_detail.sale_id == self.sales.id
        assert sales_detail.payment_id == self.sales.id
        assert sales_detail.customer == "Customer Name"
        assert sales_detail.item_type == "Retail Item"
        assert sales_detail.retail_item_id == self.retail_item.id
        assert sales_detail.staff == "Staff Name"
        assert sales_detail.amount == 1
        assert sales_detail.gross_sales == Decimal('100.00')
        assert sales_detail.discount_type == "Discount Type"
        assert sales_detail.discount == Decimal('10.00')
        assert sales_detail.net_sales == Decimal('90.00')
        assert sales_detail.field1 == "Field1 Value"
        assert sales_detail.field2 == "Field2 Value"

    def test_seller(self):
        seller = Seller.objects.get(seller_name="Seller Name")
        self.assertIsNotNone(seller.id)
        assert seller.seller_name == "Seller Name"

    def test_salon_items(self):
        sales = Sales.objects.get(code="TestSales123")
        sales_detail = sales.sales_details_sale.filter(item_type="Salon Item").first()
        salon_item = sales_detail.salon_item

        self.assertIsNotNone(salon_item.id)
        assert salon_item.category == "Category"
        assert salon_item.number == 1
        assert salon_item.display_name == "Display Name"
        assert salon_item.norm_name == "Norm Name"
        assert salon_item.price == 100.00
        assert salon_item.tax_category == "Tax Category"
        assert salon_item.active == True
        assert salon_item.registration_date == timezone.make_aware(
            datetime(2021, 3, 22, 10, 30))
        assert salon_item.update_date == timezone.make_aware(
            datetime(2021, 3, 22, 10, 30))

    def test_emoney(self):
        sales = Sales.objects.get(code="TestSales123")
        emoney = sales.emoney.first()
        emoney_type = emoney.type

        self.assertIsNotNone(emoney_type.id)
        assert emoney_type.partner == "Partner"
        assert emoney_type.item == "Item"
        assert emoney_type.type_name == "Type Name"

        self.assertIsNotNone(emoney.id)
        assert emoney.type == emoney_type
        assert emoney.sale == self.sales
        assert emoney.usage_date == timezone.make_aware(
            datetime(2021, 3, 22, 10, 30))
        assert emoney.customer_name == "Customer Name"
        assert emoney.amount == 100.00
        assert emoney.cashier == "Cashier"


    def test_freee_deals(self):
        freee_deals = FreeeDeals.objects.get(number=12345)
        self.assertIsNotNone(freee_deals.id)
        assert freee_deals.type == "Example Type"
        assert freee_deals.number == 12345
        assert freee_deals.title == "Example Title"
        assert freee_deals.date == timezone.make_aware(datetime(2022, 3, 22))
        assert freee_deals.slip_number == 12
        assert freee_deals.debit_account == "Example Debit Account"
        assert freee_deals.debit_sub_account == "Example Debit Sub Account"
        assert freee_deals.debit_partner == "Example Debit Partner"
        assert freee_deals.debit_department == "Example Debit Department"
        assert freee_deals.debit_item == "Example Debit Item"
        assert freee_deals.debit_memo_tag == "Example Debit Memo Tag"
        assert freee_deals.debit_tax_category == "Example Debit Tax Category"
        assert freee_deals.debit_amount == 1000.00
        assert freee_deals.debit_tax_amount == 100.00
        assert freee_deals.credit_account == "Example Credit Account"
        assert freee_deals.credit_sub_account == "Example Credit Sub Account"
        assert freee_deals.credit_partner == "Example Credit Partner"
        assert freee_deals.credit_department == "Example Credit Department"
        assert freee_deals.credit_item == "Example Credit Item"
        assert freee_deals.credit_memo_tag == "Example Credit Memo Tag"
        assert freee_deals.credit_tax_category == "Example Credit Tax Category"
        assert freee_deals.credit_amount == 1000.00
        assert freee_deals.credit_tax_amount == 100.00
        assert freee_deals.summary == "Example Summary"


    def test_hp(self):
        sale = Sales.objects.get(code="TestSales123")
        hp = sale.hp
        assert hp.sales_date == timezone.make_aware(datetime(2022, 3, 22))
        assert hp.net_sales == 1000.00
        assert hp.points == 200.00

    def test_omron(self):
        omron = Omron.objects.get(slip_number="SL123456")
        self.assertIsNotNone(omron.id)
        assert omron.handling_date == timezone.make_aware(
            datetime(2022, 3, 22))
        assert omron.credit_company_code == "12345"
        assert omron.credit_company_name == "CreditCompany"
        assert omron.payment_category == "PaymentCategory"
        assert omron.payment_name == "PaymentName"
        assert omron.installment_count_gift_value == 12
        assert omron.gift_ticket_quantity == 5
        assert omron.slip_number == "SL123456"
        assert omron.sales_amount == 1500.00
        assert omron.scheduled_payment_date1 == timezone.make_aware(
            datetime(2022, 4, 22))
        assert omron.scheduled_payment_date2 == timezone.make_aware(
            datetime(2022, 5, 22))


    def test_payments(self):
        payment = Payments.objects.get(payment_id="PAY12345")
        self.assertIsNotNone(payment.id)
        assert payment.payment_id == "PAY12345"
        assert payment.sale == self.sales
        assert payment.date == timezone.make_aware(datetime(2022, 3, 22))
        assert payment.time == timezone.make_aware(
            datetime(2022, 3, 22, 10, 30))
        assert payment.total_collected == 1500.00
        assert payment.fees == 50.00
        assert payment.net_total == 1450.00
        assert payment.customer_name == "John Doe"
        assert payment.card_brand == "Visa"
        assert payment.pan_suffix == "1234"
        assert payment.deposit_date == "2022-03-23"
        assert payment.fee_percentage_rate == 3.00
        assert payment.field1 == "SampleField1"

    def test_retail_items(self):
        retail_item = RetailItems.objects.get(category="Electronics")
        self.assertIsNotNone(retail_item.id)
        assert retail_item.category == "Electronics"
        assert retail_item.number == 1
        assert retail_item.display_name == "Smartphone"
        assert retail_item.norm_name == "Smartphone"
        assert retail_item.price == 900.00
        assert retail_item.cost == 600.00
        assert retail_item.vat_type == "Standard"
        assert retail_item.vat_rate == 10.00
        assert retail_item.product_category == "Phone"
        assert retail_item.supplier_name == "Phone Manufacturer"
        assert retail_item.seller == self.seller
        assert retail_item.active == True
        assert retail_item.registration_date == timezone.make_aware(
            datetime(2022, 1, 1))
        assert retail_item.update_date == timezone.make_aware(
            datetime(2022, 2, 15))
