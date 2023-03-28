from rest_framework import serializers
from .models import Emoney, EmoneyTypes, FreeeDeals, HPs, OmronTransactions, Payments, RetailItems, Sales, SalesDetails, Sellers, SalonItems

class EMoneySerializer(serializers.ModelSerializer):
    class Meta:
        model = Emoney
        fields = ('id', 'type_id', 'sales_id', 'usage_date', 'customer_name', 'amount', 'cashier')

class EmoneyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmoneyTypes
        fields = ('id', 'partner', 'item', 'type_name')

class FreeeDealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeeDeals
        fields = ('type', 'number', 'title', 'date', 'slip_number', 'debit_account', 'debit_sub_account', 'debit_partner', 'debit_department', 'debit_item', 'debit_memo_tag', 'debit_tax_category', 'debit_amount', 'debit_tax_amount', 'credit_account', 'credit_sub_account', 'credit_partner', 'credit_department', 'credit_item', 'credit_memo_tag', 'credit_tax_category', 'credit_amount', 'credit_tax_amount', 'summary')

class HPSerializer(serializers.ModelSerializer):
    class Meta:
        model = HPs
        fields = ('id', 'sales_id', 'sales_date', 'net_sales', 'points')

class OMRONSerializer(serializers.ModelSerializer):
    class Meta:
        model = OmronTransactions
        fields = ('id', 'handling_date', 'credit_company_code', 'credit_company_name', 'payment_category', 'payment_name', 'installment_count_gift_value', 'gift_ticket_quantity', 'slip_number', 'sales_amount', 'scheduled_payment_date1', 'scheduled_payment_date2')

class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = ('payment_id', 'sales_id', 'date', 'time', 'total_collected', 'fees', 'net_total', 'customer_name', 'card_brand', 'pan_suffix', 'deposit_date', 'fee_percentage_rate', 'field1')

class RetailItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RetailItems
        fields = ('id', 'category', 'number', 'display_name', 'norm_name', 'price', 'cost', 'vat_type', 'vat_rate', 'product_category', 'supplier_name', 'seller', 'active', 'registration_date', 'update_date')

class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = ('id', 'sales_id', 'customer', 'from_time', 'to_time', 'gross_salon_sales', 'gross_retail_sales', 'total_gross_sales', 'total_salon_discount', 'retail_discount', 'service_net_sales', 'retail_net_sales', 'total_net_sales', 'cash', 'card', 'card_type', 'em', 'prepaid', 'credit', 'tax', 'comment')

class SalesDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesDetails
        fields = ('id', 'sale_id', 'payment_id', 'customer', 'item_type', 'item_id', 'staff', 'amount', 'gross_sales', 'discount_type', 'discount', 'net_sales', 'field1', 'field2')

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sellers
        fields = ('id', 'seller_name')

class SalonItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalonItems
        fields = ('id', 'category', 'number', 'display_name', 'norm_name', 'price', 'tax_category', 'active', 'registration_date', 'update_date')
