from django.urls import path
from . import views

urlpatterns = [
    path('emoney/', views.EMoneyListCreateView.as_view(), name='emoney_list_create'),
    path('emoney-types/', views.EmoneyTypeListCreateView.as_view(), name='emoney_types_list_create'),
    path('freee-deals/', views.FreeeDealsListCreateView.as_view(), name='freeedeals_list_create'),
    path('hps/', views.HPListCreateView.as_view(), name='hp_list_create'),
    path('omron-transactions/', views.OMRONListCreateView.as_view(), name='omron_list_create'),
    path('payments/', views.PaymentsListCreateView.as_view(), name='payments_list_create'),
    path('retail-items/', views.RetailItemsListCreateView.as_view(), name='retailitems_list_create'),
    path('sales/', views.SalesListCreateView.as_view(), name='sales_list_create'),
    path('sales-items/', views.SalesItemsListCreateView.as_view(), name='salesitems_list_create'),
    path('seller/', views.SellerListCreateView.as_view(), name='seller_list_create'),
    path('salon-items/', views.SalonItemsListCreateView.as_view(), name='salonitems_list_create'),
]
