from django.urls import path
from . import views

urlpatterns = [
    path('sales/', views.SalesListCreateView.as_view(), name='sales_list_create'),
    path('sales/<int:pk>/', views.SalesRetrieveUpdateDestroyView.as_view(), name='sales_retrieve_update_destroy'),
    path('sales/<int:sale_id>/items/', views.SalesItemsListCreateView.as_view(), name='sales_items_list_create'),
    path('sales/<int:sale_id>/items/<int:pk>/', views.SalesItemsRetrieveUpdateDestroyView.as_view(), name='sales_items_retrieve_update_destroy'),
    path('sales/<int:sale_id>/emoney/', views.EMoneyListCreateView.as_view(), name='emoney_list_create'),
    path('sales/<int:sale_id>/emoney/<int:pk>/', views.EmoneyRetrieveUpdateDestroyView.as_view(), name='emoney_retrieve_update_destroy'),
    path('sales/<int:sale_id>/payments/', views.PaymentsListCreateView.as_view(), name='payments_list_create'),
    path('sales/<int:sale_id>/payments/<int:pk>/', views.PaymentsRetrieveUpdateDestroyView.as_view(), name='payments_retrieve_update_destroy'),

    path('seller/', views.SellerListCreateView.as_view(), name='seller_list_create'),
    path('seller/<int:pk>/', views.SellerRetrieveUpdateDestroyView.as_view(), name='seller_retrieve_update_destroy'),
    path('emoney-types/', views.EmoneyTypeListCreateView.as_view(), name='emoney_types_list_create'),
    path('emoney-types/<int:pk>/', views.EmoneyTypeRetrieveUpdateDestroyView.as_view(), name='emoney_types_retrieve_update_destroy'),
    path('emoney/', views.EmoneyListView.as_view(), name='emoney_list'),
    path('emoney/<int:pk>/', views.EmoneyRetrieveUpdateDestroyView.as_view(), name='emoney_retrieve_update_destroy'),
    path('freee-deals/', views.FreeeDealsListCreateView.as_view(), name='freee_deals_list_create'),
    path('freee-deals/<int:pk>/', views.FreeeDealsRetrieveUpdateDestroyView.as_view(), name='freee_deals_retrieve_update_destroy'),
    path('hps/', views.HPListCreateView.as_view(), name='hp_list_create'),
    path('hps/<int:pk>/', views.HPRetrieveUpdateDestroyView.as_view(), name='hp_retrieve_update_destroy'),
    path('omron-transactions/', views.OMRONListCreateView.as_view(), name='omron_transactions_list_create'),
    path('omron-transactions/<int:pk>/', views.OMRONRetrieveUpdateDestroyView.as_view(), name='omron_transactions_retrieve_update_destroy'),
    path('payments/', views.PaymentsListView.as_view(), name='payments_list'),
    path('payments/<int:pk>/', views.PaymentsRetrieveUpdateDestroyView.as_view(), name='payments_retrieve_update_destroy'),
    path('salon-items/', views.SalonItemsListCreateView.as_view(), name='salon_items_list_create'),
    path('salon-items/<int:pk>/', views.SalonItemsRetrieveUpdateDestroyView.as_view(), name='salon_items_retrieve_update_destroy'),
    path('retail-items/', views.RetailItemsListCreateView.as_view(), name='retail_items_list_create'),
    path('retail-items/<int:pk>/', views.RetailItemsRetrieveUpdateDestroyView.as_view(), name='retail_items_retrieve_update_destroy'),
]
