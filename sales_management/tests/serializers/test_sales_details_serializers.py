import pytest
from sales_management.models import RetailItems, Sales, SalesItems, SalonItems
from sales_management.serializers import SalesItemsCreateUpdateSerializer, SalesItemsRetrieveSerializer, SalonItemsSerializer
from sales_management.tests.test_utils import load_test_data


@pytest.mark.django_db
def test_create(load_test_data):
    data = {
        "customer": "customer1",
        "item_type": "type1",
        "staff": "staff1",
        "amount": 5,
        "gross_sales": 100.00,
        "discount_type": "percentage",
        "discount": 10.00,
        "net_sales": 90.00,
        "field1": "field_value1",
        "field2": "field_value2",
        "sale": 1,
        "payment": 1,
        "salon_item": 1,
        "retail_item": 1,
    }
    sales_items_count = SalesItems.objects.count()
    salon_item_count = SalonItems.objects.count()
    retail_item_count = RetailItems.objects.count()

    serializer = SalesItemsCreateUpdateSerializer(data=data)
    print(serializer.errors if not serializer.is_valid() else "")
    assert  serializer.is_valid()
    serializer.save()
    assert SalesItems.objects.count() == 1 + sales_items_count

    # Check if the related objects are not changed
    assert SalonItems.objects.count() == salon_item_count    
    assert RetailItems.objects.count() == retail_item_count

@pytest.mark.django_db
def test_update(load_test_data):
    data = {
        "customer": "customer1",
        "item_type": "type1",
        "staff": "staff1",
        "amount": 5,
        "gross_sales": 100.00,
        "discount_type": "percentage",
        "discount": 10.00,
        "net_sales": 90.00,
        "field1": "field_value1",
        "field2": "field_value2",
        "sale": 2,
        "payment": 3,
        "salon_item": 1, 
        "retail_item": 1,
    }
    detail_count = SalesItems.objects.count()
    salon_item_count = SalonItems.objects.count()
    retail_item_count = RetailItems.objects.count()

    sales_items_org = SalesItems.objects.get(id=1)
    serializer = SalesItemsCreateUpdateSerializer(sales_items_org, data=data)
    print(serializer.errors if not serializer.is_valid() else "")
    assert serializer.is_valid()
    serializer.save()
    sales_items = SalesItems.objects.get(id=1)
    assert sales_items.customer == "customer1"
    assert sales_items.item_type == "type1"
    assert sales_items.staff == "staff1"
    assert sales_items.amount == 5
    assert sales_items.gross_sales == 100.00
    assert sales_items.discount_type == "percentage"
    assert sales_items.discount == 10.00
    assert sales_items.net_sales == 90.00
    assert sales_items.field1 == "field_value1"
    assert sales_items.field2 == "field_value2"
    assert sales_items.sale == Sales.objects.get(id=2)
    assert sales_items.payment == Sales.objects.get(id=3)
    assert sales_items.salon_item == SalonItems.objects.get(id=1)
    assert sales_items.retail_item == RetailItems.objects.get(id=1)

    # check if the number of records in the database is the same
    assert SalesItems.objects.count() == detail_count
    assert SalonItems.objects.count() == salon_item_count
    assert RetailItems.objects.count() == retail_item_count

@pytest.mark.django_db
def test_retrieve(load_test_data):
    sales_items = SalesItems.objects.get(id=13)
    serializer = SalesItemsRetrieveSerializer(sales_items)
    # CREATE TABLE IF NOT EXISTS "sales_items" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "customer" varchar(255) NULL, "item_type" varchar(255) NULL, "staff" varchar(255) NULL, "amount" integer NULL, "gross_sales" decimal NULL, "discount_type" varchar(255) NULL, "discount" decimal NULL, "net_sales" decimal NULL, "field1" varchar(255) NULL, "field2" varchar(255) NULL, "retail_item_id" bigint NULL REFERENCES "retail_items" ("id") DEFERRABLE INITIALLY DEFERRED, "payment_id" bigint NULL REFERENCES "sales" ("id") DEFERRABLE INITIALLY DEFERRED, "sale_id" bigint NULL REFERENCES "sales" ("id") DEFERRABLE INITIALLY DEFERRED, "salon_item_id" bigint NULL REFERENCES "salon_items" ("id") DEFERRABLE INITIALLY DEFERRED);
    # INSERT INTO sales_items VALUES(13,'15b78ea1c1c780328bca41ad0c5d9d7bb44cb015','技術','ebf749a8001319793e6bd76350424a7c2af23d29',1,2200,'ヒルズシール割引(技術)',220,1980,'da39a3ee5e6b4b0d3255bfef95601890afd80709','da39a3ee5e6b4b0d3255bfef95601890afd80709',NULL,22,22,348);
    assert serializer.data["id"] == 13
    assert serializer.data["customer"] == "15b78ea1c1c780328bca41ad0c5d9d7bb44cb015"
    assert serializer.data["item_type"] == "技術"
    assert serializer.data["staff"] == "ebf749a8001319793e6bd76350424a7c2af23d29"
    assert serializer.data["amount"] == 1
    assert serializer.data["gross_sales"] == "2200.00"
    assert serializer.data["discount_type"] == "ヒルズシール割引(技術)"
    assert serializer.data["discount"] == "220.00"
    assert serializer.data["net_sales"] == "1980.00"
    assert serializer.data["field1"] == "da39a3ee5e6b4b0d3255bfef95601890afd80709"
    assert serializer.data["field2"] == "da39a3ee5e6b4b0d3255bfef95601890afd80709"
    assert serializer.data["sale"] == 22
    assert serializer.data["payment"] == 22
    assert serializer.data["salon_item"] == SalonItemsSerializer(SalonItems.objects.get(id=348)).data
    assert serializer.data["retail_item"] == None

