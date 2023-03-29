from rest_framework import generics
from .models import Emoney, EmoneyTypes, FreeeDeals, HPs, OmronTransactions, Payments, RetailItems, Sales, SalesDetails, Sellers, SalonItems
from .serializers import EMoneySerializer, EmoneyTypeSerializer, FreeeDealsSerializer, HPsSerializer, OmronTransactionsSerializer, PaymentsSerializer, RetailItemsSerializer, SalesSerializer, SalesDetailsSerializer, SellersSerializer, SalonItemsSerializer

class EMoneyListCreateView(generics.ListCreateAPIView):
    queryset = Emoney.objects.all()
    serializer_class = EMoneySerializer

class EmoneyTypeListCreateView(generics.ListCreateAPIView):
    queryset = EmoneyTypes.objects.all()
    serializer_class = EmoneyTypeSerializer

class FreeeDealsListCreateView(generics.ListCreateAPIView):
    queryset = FreeeDeals.objects.all()
    serializer_class = FreeeDealsSerializer

class HPListCreateView(generics.ListCreateAPIView):
    queryset = HPs.objects.all()
    serializer_class = HPsSerializer

class OMRONListCreateView(generics.ListCreateAPIView):
    queryset = OmronTransactions.objects.all()
    serializer_class = OmronTransactionsSerializer

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
    queryset = Sellers.objects.all()
    serializer_class = SellersSerializer

class SalonItemsListCreateView(generics.ListCreateAPIView):
    queryset = SalonItems.objects.all()
    serializer_class = SalonItemsSerializer
