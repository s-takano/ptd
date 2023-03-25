from rest_framework import serializers
from .models import Emoney, EmoneyType, FreeeDeals, Hp, Omron, Payments, RetailItems, Sales, SalesDetails, Seller, SalonItems

class EMoneySerializer(serializers.ModelSerializer):
    class Meta:
        model = Emoney
        fields = ('id', 'type_id', 'sales_id', 'usage_date', 'customer_name', 'amount', 'cashier')

class EMTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmoneyType
        fields = ('id', 'trading_partner', 'product', 'type_name')

class FreeeDealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeeDeals
        fields = ('type', 'no', 'headline', 'date', 'voucher_number', 'debit_account', 'debit_sub_account', 'debit_partner', 'debit_department', 'debit_product', 'debit_memo_tag', 'debit_tax_category', 'debit_amount', 'debit_tax_amount', 'credit_account', 'credit_sub_account', 'credit_partner', 'credit_department', 'credit_product', 'credit_memo_tag', 'credit_tax_category', 'credit_amount', 'credit_tax_amount', 'summary')

class HPSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hp
        fields = ('id', 'sales_id', 'sales_date', 'net_sales', 'points')

class OMRONSerializer(serializers.ModelSerializer):
    class Meta:
        model = Omron
        fields = ('id', 'handling_date', 'credit_company_code', 'credit_company_name', 'payment_type', 'payment_name', 'installments_gift_value', 'gift_ticket_quantity', 'voucher_number', 'sales_amount', 'deposit_due_date_1', 'deposit_due_date_2')

class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = ('payment_id', 'sales_id', 'date', 'time', 'total_collected', 'fees', 'net_total', 'customer_name', 'card_brand', 'pan_suffix', 'deposit_date', 'fee_percentage_rate', 'field1')

class RetailItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RetailItems
        fields = ('id', 'category', 'no', 'display_name', 'norm_name', 'price', 'cost', 'vat_type', 'vat_rate', 'product_type', 'supplier_name', 'seller', 'active', 'registration_date', 'update_date')

class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = ('id', 'sales_id', 'customer', 'sales_date', 'from_time', 'to_time', 'gross_salon_sales', 'gross_retail_sales', 'total_gross_sales', 'total_salon_discount', 'retail_discount', 'service_net_sales', 'retail_net_sales', 'total_net_sales', 'cash', 'card', 'card_type', 'em', 'prepaid', 'credit', 'tax', 'comment')

class SalesDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesDetails
        fields = ('id', 'sale_id', 'payment_id', 'customer', 'item_type', 'item_id', 'staff', 'amount', 'gross_sales', 'discount_type', 'discount', 'net_sales', 'field1', 'field2')

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ('id', 'seller_name')

class SalonItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalonItems
        fields = ('id', 'category', 'no', 'display_name', 'norm_name', 'price', 'tax_type', 'active', 'registration_date', 'update_date')
