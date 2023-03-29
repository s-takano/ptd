from django.test import TestCase
from django.utils import timezone
from sales_management.models import Sales, Sellers, FreeeDeals, OmronTransactions, SalesDetails, Payments, HPs, Emoney, EmoneyTypes
from sales_management.serializers import SalesSerializer, SellersSerializer, FreeeDealsSerializer, OmronTransactionsSerializer, SalesDetailsSerializer, PaymentsSerializer, HPsSerializer, EMoneySerializer, EmoneyTypeSerializer

class SalesSerializerTest(TestCase):
    def test_create(self):
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
        self.assertTrue(serializer.is_valid())
        serializer.save()
        self.assertEqual(Sales.objects.count(), 1+count)

