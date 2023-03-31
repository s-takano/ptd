from decimal import Decimal
from django.test import TestCase
from django.utils import timezone
import pytest
from sales_management.models import Sales
from sales_management.serializers import SalesSerializer
from sales_management.tests.test_utils import is_valid_datetime, load_test_data

@pytest.mark.django_db()
def test_create(load_test_data):
    data = {
        'code': "1",
        'customer': 'customer',
        'from_time': timezone.now(),
        'to_time': timezone.now(),
        'gross_salon_sales': 1,
        'gross_retail_sales': 1,
        'total_gross_sales': 1,
        'total_salon_discount': 1,
        'retail_discount': 1,
        'service_net_sales': 1,
        'retail_net_sales': 1,
        'total_net_sales': 1,
        'cash': 1,
        'card': 1,
        'card_type': 'card_type',
        'em': 1,
        'prepaid': 1,
        'credit': 1,
        'tax': 1,
        'comment': 'comment',
    }
    count = Sales.objects.count()
    serializer = SalesSerializer(data=data)
    assert serializer.is_valid()
    serializer.save()
    assert Sales.objects.count()== 1+count

@pytest.mark.django_db()
def test_update(load_test_data):
    data = {
        'code': "S202207080013",
        'customer': 'customer',
        'from_time': timezone.now(),
        'to_time': timezone.now(),
        'gross_salon_sales': 1,
        'gross_retail_sales': 1,
        'total_gross_sales': 1,
        'total_salon_discount': 1,
        'retail_discount': 1,
        'service_net_sales': 1,
        'retail_net_sales': 1,
        'total_net_sales': 1,
        'cash': 1,
        'card': 1,
        'card_type': 'card_type',
        'em': 1,
        'prepaid': 1,
        'credit': 1,
        'tax': 1,
        'comment': 'comment',
    }
    sales = Sales.objects.get(code="S202207080013")
    serializer = SalesSerializer(sales, data=data)
    assert serializer.is_valid()
    serializer.save()
    sales = Sales.objects.get(code="S202207080013")
    assert sales.code== "S202207080013"
    assert sales.customer== "customer"
    assert sales.from_time== data['from_time']
    assert sales.to_time == data['to_time']
    assert sales.gross_salon_sales == 1
    assert sales.gross_retail_sales == 1
    assert sales.total_gross_sales == 1
    assert sales.total_salon_discount == 1
    assert sales.retail_discount == 1
    assert sales.service_net_sales == 1
    assert sales.retail_net_sales == 1
    assert sales.total_net_sales == 1
    assert sales.cash == 1
    assert sales.card == 1
    assert sales.card_type == "card_type"
    assert sales.em == 1
    assert sales.prepaid == 1
    assert sales.credit == 1
    assert sales.tax == 1
    assert sales.comment == "comment"

@pytest.mark.django_db()
def test_delete(load_test_data):
    initial_count = Sales.objects.count()
    sales = Sales.objects.get(code="S202207080013")
    sales.delete()
    assert Sales.objects.count()== initial_count-1

@pytest.mark.django_db()
def test_get(load_test_data):
    sales = Sales.objects.get(code="S202207080013")
    print(sales.from_time)
    serializer = SalesSerializer(sales)
    assert serializer.data['code'] == "S202207080013"
    assert serializer.data['customer'] == "d757a1ab26d9e6975a0c9206d49c5023cbe33e3b"
    assert is_valid_datetime(serializer.data['from_time'], "2022-07-08T03:17:00")
    assert is_valid_datetime(serializer.data['to_time'], "2022-07-08 03:18:00")
    assert Decimal(serializer.data['gross_salon_sales']) == Decimal("4400")
    assert Decimal(serializer.data['gross_retail_sales']) == Decimal("22000")
    assert Decimal(serializer.data['total_gross_sales']) == Decimal("26400")
    assert Decimal(serializer.data['total_salon_discount']) == Decimal("0")
    assert Decimal(serializer.data['retail_discount']) == Decimal("0")
    assert Decimal(serializer.data['service_net_sales']) == Decimal("4400")
    assert Decimal(serializer.data['retail_net_sales']) == Decimal("22000")
    assert Decimal(serializer.data['total_net_sales']) == Decimal("26400")
    assert Decimal(serializer.data['cash']) == Decimal("0")
    assert Decimal(serializer.data['card']) == Decimal("23400")
    assert serializer.data['card_type'] == "[クレジット]"
    assert Decimal(serializer.data['em']) == Decimal("3000")
    assert Decimal(serializer.data['prepaid']) == Decimal("0")
    assert Decimal(serializer.data['credit']) == Decimal("0")
    assert Decimal(serializer.data['tax']) == Decimal("2400")
    assert serializer.data['comment'] == "da39a3ee5e6b4b0d3255bfef95601890afd80709"
    # check details exist
    assert len(serializer.data['details']) == 2
    # check emoney exist
    assert len(serializer.data['emoney']) == 1
    # check payments exist
    assert len(serializer.data['payments']) == 1
    # check hps exist
    assert len(serializer.data['hps']) == 0

