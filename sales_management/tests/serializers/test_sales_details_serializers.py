import pytest
from sales_management.models import RetailItems, Sales, SalesItems, SalonItems
from sales_management.serializers import SalesItemsSerializer
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
    count = SalesItems.objects.count()
    serializer = SalesItemsSerializer(data=data)
    assert serializer.is_valid()
    serializer.save()
    assert SalesItems.objects.count() == 1+count

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
        "salon_item": {"id": 1}, 
        "retail_item": {"id": 1},
    }
    detail_count = SalesItems.objects.count()
    salon_item_count = SalonItems.objects.count()
    retail_item_count = RetailItems.objects.count()

    sales_items = SalesItems.objects.get(id=1)
    serializer = SalesItemsSerializer(sales_items, data=data)
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
