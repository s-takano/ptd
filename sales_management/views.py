from rest_framework import generics, status
from .models import Emoney, EmoneyTypes, FreeeDeals, HPs, OmronTransactions, Payments, RetailItems, Sales, SalesItems, Sellers, SalonItems
from .serializers import EMoneyRetrieveSerializer,EMoneyCreateListSerializer, EmoneyTypeSerializer, FreeeDealsSerializer, HPsSerializer, OmronTransactionsSerializer, PaymentsRetrieveSerializer, PaymentsListCreateSerializer, RetailItemsRetrievalSerializer, RetailItemsListCreateSerializer, SalesCreateUpdateSerializer, SalesItemsCreateUpdateSerializer, SalesItemsRetrieveSerializer, SalesRetrieveSerializer, SellersSerializer, SalonItemsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class EMoneyListCreateView(generics.ListCreateAPIView):
    serializer_class = EMoneyCreateListSerializer

    def get_queryset(self):
        if 'sale_id' not in self.kwargs:
            return Emoney.objects.all()
        sale_id = self.kwargs['sale_id']
        return Emoney.objects.filter(sale=sale_id)
    
    def post(self, request, *args, **kwargs):
        if 'sale_id' not in self.kwargs:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        sale_id = self.kwargs['sale_id']
        request.data['sale'] = sale_id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class EmoneyListView(generics.ListAPIView):
    queryset = Emoney.objects.all()
    serializer_class = EMoneyRetrieveSerializer

class EmoneyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Emoney.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EMoneyRetrieveSerializer
        return EMoneyCreateListSerializer

class EmoneyTypeListCreateView(generics.ListCreateAPIView):
    queryset = EmoneyTypes.objects.all()
    serializer_class = EmoneyTypeSerializer

class EmoneyTypeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmoneyTypes.objects.all()
    serializer_class = EmoneyTypeSerializer
    

class FreeeDealsListCreateView(generics.ListCreateAPIView):
    queryset = FreeeDeals.objects.all()
    serializer_class = FreeeDealsSerializer

class FreeeDealsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FreeeDeals.objects.all()
    serializer_class = FreeeDealsSerializer

class HPListCreateView(generics.ListCreateAPIView):
    queryset = HPs.objects.all()
    serializer_class = HPsSerializer

class HPRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HPs.objects.all()
    serializer_class = HPsSerializer

class OMRONListCreateView(generics.ListCreateAPIView):
    queryset = OmronTransactions.objects.all()
    serializer_class = OmronTransactionsSerializer

class OMRONRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OmronTransactions.objects.all()
    serializer_class = OmronTransactionsSerializer
class PaymentsListCreateView(generics.ListCreateAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsListCreateSerializer

    def get_queryset(self):
        if 'sale_id' not in self.kwargs:
            return Payments.objects.all()
        sale_id = self.kwargs['sale_id']
        return Payments.objects.filter(sale=sale_id)
    
    def post(self, request, *args, **kwargs):
        if 'sale_id' not in self.kwargs:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        sale_id = self.kwargs['sale_id']
        request.data['sale'] = sale_id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class PaymentsListView(generics.ListAPIView):
    queryset = Payments.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PaymentsRetrieveSerializer
        return PaymentsListCreateSerializer

class RetailItemsListCreateView(generics.ListCreateAPIView):
    queryset = RetailItems.objects.all()
    serializer_class = RetailItemsListCreateSerializer

class RetailItemsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RetailItems.objects.all()
    serializer_class = RetailItemsRetrievalSerializer

class SalesListCreateView(generics.ListCreateAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesRetrieveSerializer

class SalesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sales.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SalesRetrieveSerializer
        elif self.request.method in ['PUT', 'PATCH']:
            return SalesCreateUpdateSerializer
        return super().get_serializer_class()


class SalesItemsListCreateView(generics.ListCreateAPIView):
    queryset = SalesItems.objects.all()
    serializer_class = SalesItemsRetrieveSerializer

class SalesItemsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SalesItems.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SalesItemsRetrieveSerializer
        elif self.request.method in ['PUT', 'PATCH']:
            return SalesItemsCreateUpdateSerializer
        return super().get_serializer_class()
    
class SellerListCreateView(generics.ListCreateAPIView):
    queryset = Sellers.objects.all()
    serializer_class = SellersSerializer

class SellerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sellers.objects.all()
    serializer_class = SellersSerializer
class SalonItemsListCreateView(generics.ListCreateAPIView):
    queryset = SalonItems.objects.all()
    serializer_class = SalonItemsSerializer

class SalonItemsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SalonItems.objects.all()
    serializer_class = SalonItemsSerializer

class PaymentsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsRetrieveSerializer