from rest_framework import generics
from .models import Emoney, EmoneyType, FreeeDeals, Hp, Omron, Payments, RetailItems, Sales, SalesDetails, Seller, SalonItems
from .serializers import EMoneySerializer, EmoneyTypeSerializer, FreeeDealsSerializer, HPSerializer, OMRONSerializer, PaymentsSerializer, RetailItemsSerializer, SalesSerializer, SalesDetailsSerializer, SellerSerializer, SalonItemsSerializer

class EMoneyListCreateView(generics.ListCreateAPIView):
    queryset = Emoney.objects.all()
    serializer_class = EMoneySerializer

class EmoneyTypeListCreateView(generics.ListCreateAPIView):
    queryset = EmoneyType.objects.all()
    serializer_class = EmoneyTypeSerializer

class FreeeDealsListCreateView(generics.ListCreateAPIView):
    queryset = FreeeDeals.objects.all()
    serializer_class = FreeeDealsSerializer

class HPListCreateView(generics.ListCreateAPIView):
    queryset = Hp.objects.all()
    serializer_class = HPSerializer

class OMRONListCreateView(generics.ListCreateAPIView):
    queryset = Omron.objects.all()
    serializer_class = OMRONSerializer

class PaymentsListCreateView(generics.ListCreateAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer

class RetailItemsListCreateView(generics.ListCreateAPIView):
    queryset = RetailItems.objects.all()
    serializer_class = RetailItemsSerializer

class SalesListCreateView(generics.ListCreateAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer

class SalesDetailsListCreateView(generics.ListCreateAPIView):
    queryset = SalesDetails.objects.all()
    serializer_class = SalesDetailsSerializer

class SellerListCreateView(generics.ListCreateAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

class SalonItemsListCreateView(generics.ListCreateAPIView):
    queryset = SalonItems.objects.all()
    serializer_class = SalonItemsSerializer
