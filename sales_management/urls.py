from django.urls import path
from . import views

urlpatterns = [
    path('emoney/', views.EMoneyListCreateView.as_view(), name='emoney_list_create'),
    path('emtype/', views.EmoneyTypeListCreateView.as_view(), name='emtype_list_create'),
    path('freeedeals/', views.FreeeDealsListCreateView.as_view(), name='freeedeals_list_create'),
    path('hp/', views.HPListCreateView.as_view(), name='hp_list_create'),
    path('omron/', views.OMRONListCreateView.as_view(), name='omron_list_create'),
    path('payments/', views.PaymentsListCreateView.as_view(), name='payments_list_create'),
    path('retailitems/', views.RetailItemsListCreateView.as_view(), name='retailitems_list_create'),
    path('sales/', views.SalesListCreateView.as_view(), name='sales_list_create'),
    path('salesdetails/', views.SalesDetailsListCreateView.as_view(), name='salesdetails_list_create'),
    path('seller/', views.SellerListCreateView.as_view(), name='seller_list_create'),
    path('salonitems/', views.SalonItemsListCreateView.as_view(), name='salonitems_list_create'),
]
