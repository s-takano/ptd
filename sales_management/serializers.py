from rest_framework import serializers
from .models import Emoney, EmoneyTypes, FreeeDeals, HPs, OmronTransactions, Payments, RetailItems, Sales, SalesDetails, Sellers, SalonItems


class EmoneyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmoneyTypes
        fields = ('id', 'partner', 'item', 'type_name')

class EMoneySerializer(serializers.ModelSerializer):
    sale = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Sales.objects.all())
    type = EmoneyTypeSerializer(read_only=False)
    class Meta:
        model = Emoney
        fields = ('id', 'type', 'sale', 'usage_date', 'customer_name', 'amount', 'cashier')

class FreeeDealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeeDeals
        fields = ('type', 'number', 'title', 'date', 'slip_number', 'debit_account', 'debit_sub_account', 'debit_partner', 'debit_department', 'debit_item', 'debit_memo_tag', 'debit_tax_category', 'debit_amount', 'debit_tax_amount', 'credit_account', 'credit_sub_account', 'credit_partner', 'credit_department', 'credit_item', 'credit_memo_tag', 'credit_tax_category', 'credit_amount', 'credit_tax_amount', 'summary')

class HPsSerializer(serializers.ModelSerializer):
    sale = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Sales.objects.all())
    class Meta:
        model = HPs
        fields = ('id', 'sale', 'sales_date', 'net_sales', 'points')

class OmronTransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OmronTransactions
        fields = ('id', 'handling_date', 'credit_company_code', 'credit_company_name', 'payment_category', 'payment_name', 'installment_count_gift_value', 'gift_ticket_quantity', 'slip_number', 'sales_amount', 'scheduled_payment_date1', 'scheduled_payment_date2')

class PaymentsSerializer(serializers.ModelSerializer):
    sale = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Sales.objects.all())
    payment = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Sales.objects.all())
    class Meta:
        model = Payments
        fields = ('payment', 'sale', 'date', 'time', 'total_collected', 'fees', 'net_total', 'customer_name', 'card_brand', 'pan_suffix', 'deposit_date', 'fee_percentage_rate', 'field1')

class SellersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sellers
        fields = ('id', 'seller_name')


class RetailItemsSerializer(serializers.ModelSerializer):
    seller = SellersSerializer(read_only=True)
    class Meta:
        model = RetailItems
        fields = ('id', 'category', 'number', 'display_name', 'norm_name', 'price', 'cost', 'vat_type', 'vat_rate', 'product_category', 'supplier_name', 'seller', 'active', 'registration_date', 'update_date')

class SalonItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalonItems
        fields = ('id', 'category', 'number', 'display_name', 'norm_name', 'price', 'tax_category', 'active', 'registration_date', 'update_date')

class SalesDetailsSerializer(serializers.ModelSerializer):
    sale = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Sales.objects.all())
    payment = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Sales.objects.all())

    salon_item = SalonItemsSerializer(read_only=True)
    retail_item = RetailItemsSerializer(read_only=True)
    class Meta:
        model = SalesDetails
        fields = ('id', 'sale', 'payment', 'customer', 'item_type', 'salon_item', 'retail_item', 'staff', 'amount', 'gross_sales', 'discount_type', 'discount', 'net_sales', 'field1', 'field2')

class SalesSerializer(serializers.ModelSerializer):
    details = SalesDetailsSerializer(many=True, read_only=True)
    emoney = EMoneySerializer(many=True, read_only=True)
    hps = HPsSerializer(many=True, read_only=True)
    payments = PaymentsSerializer(many=True, read_only=True)

    class Meta:
        model = Sales
        fields = ('id', 'code', 'customer', 'from_time', 'to_time', 'gross_salon_sales', 'gross_retail_sales', 'total_gross_sales', 'total_salon_discount', 'retail_discount', 'service_net_sales', 'retail_net_sales', 'total_net_sales', 'cash', 'card', 'card_type', 'em', 'prepaid', 'credit', 'tax', 'comment', 'hps', 'details', 'emoney', 'payments', 'details')
