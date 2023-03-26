from django.db import models


class FreeeDeals(models.Model):
    # 種別:Text(255) False
    type = models.CharField(max_length=255, null=True)
    # No:Long(4) False
    number = models.BigIntegerField(null=True)
    # 表題行:Text(255) False
    title = models.CharField(max_length=255, null=True)
    # 日付:Date/Time(8) False
    date = models.DateTimeField(null=True)
    # 伝票番号:Integer(2) False
    slip_number = models.IntegerField(null=True)
    # 借方勘定科目:Text(255) False
    debit_account = models.CharField(max_length=255, null=True)
    # 借方補助科目:Text(255) False
    debit_sub_account = models.CharField(max_length=255, null=True)
    # 借方取引先:Text(255) False
    debit_partner = models.CharField(max_length=255, null=True)
    # 借方部門:Text(255) False
    debit_department = models.CharField(max_length=255, null=True)
    # 借方品目:Text(255) False
    debit_item = models.CharField(max_length=255, null=True)
    # 借方メモタグ:Text(255) False
    debit_memo_tag = models.CharField(max_length=255, null=True)
    # 借方税区分:Text(255) False
    debit_tax_category = models.CharField(max_length=255, null=True)
    # 借方金額:Currency(8) False
    debit_amount = models.DecimalField(
        max_digits=19, decimal_places=2, null=True)
    # 借方税額:Currency(8) False
    debit_tax_amount = models.DecimalField(
        max_digits=19, decimal_places=2, null=True)
    # 貸方勘定科目:Text(255)

    # 貸方勘定科目:Text(255) False
    credit_account = models.CharField(max_length=255, null=True)
    # 貸方補助科目:Text(255) False
    credit_sub_account = models.CharField(max_length=255, null=True)
    # 貸方取引先:Text(255) False
    credit_partner = models.CharField(max_length=255, null=True)
    # 貸方部門:Text(255) False
    credit_department = models.CharField(max_length=255, null=True)
    # 貸方品目:Text(255) False
    credit_item = models.CharField(max_length=255, null=True)
    # 貸方メモタグ:Text(255) False
    credit_memo_tag = models.CharField(max_length=255, null=True)
    # 貸方税区分:Text(255) False
    credit_tax_category = models.CharField(max_length=255, null=True)
    # 貸方金額:Currency(8) False
    credit_amount = models.DecimalField(
        max_digits=19, decimal_places=2, null=True)
    # 貸方税額:Currency(8) False
    credit_tax_amount = models.DecimalField(
        max_digits=19, decimal_places=2, null=True)
    # 摘要:Text(255) False
    summary = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'freee_deals'


class Omron(models.Model):
    # ID:Long(4) False
    id = models.BigAutoField(primary_key=True)
    # お取扱日:Date/Time(8) False
    handling_date = models.DateTimeField(null=True)
    # クレジット会社コード:Text(255) False
    credit_company_code = models.CharField(max_length=255, null=True)
    # クレジット会社名:Text(255) False
    credit_company_name = models.CharField(max_length=255, null=True)
    # 支払区分:Text(255) False
    payment_category = models.CharField(max_length=255, null=True)
    # 支払名称:Text(255) False
    payment_name = models.CharField(max_length=255, null=True)
    # 分割回数／ギフト券額面:Integer(2) False
    installment_count_gift_value = models.IntegerField(null=True)
    # ギフト券枚数:Integer(2) False
    gift_ticket_quantity = models.IntegerField(null=True)
    # 伝票番号:Text(255) False
    slip_number = models.CharField(max_length=255, null=True)
    # 売上金額:Currency(8) False

    # 売上金額:Currency(8) False
    sales_amount = models.DecimalField(
        max_digits=19, decimal_places=2, null=True)
    # 入金予定日１:Date/Time(8) False
    scheduled_payment_date1 = models.DateTimeField(null=True)
    # 入金予定日２:Date/Time(8) False
    scheduled_payment_date2 = models.DateTimeField(null=True)

    class Meta:
        db_table = 'omron'


class SalonItems(models.Model):
    # ID:Long(4) False
    id = models.BigAutoField(primary_key=True)
    # Category:Text(255) False
    category = models.CharField(max_length=255, null=True)
    # No:Integer(2) False
    number = models.IntegerField(null=True)
    # DisplayName:Text(255) False
    display_name = models.CharField(max_length=255, null=True)
    # NormName:Text(255) False
    norm_name = models.CharField(max_length=255, null=True)
    # Price:Currency(8) False
    price = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    # 消費税区分:Text(255) False
    tax_category = models.CharField(max_length=255, null=True)
    # Active:Boolean(1) False
    active = models.BooleanField(null=True)
    # 登録日付:Date/Time(8) False
    registration_date = models.DateTimeField(null=True)
    # 更新日付:Date/Time(8) False
    update_date = models.DateTimeField(null=True)

    class Meta:
        db_table = 'salon_items'


class Seller(models.Model):
    # ID:Long(4) False
    id = models.BigAutoField(primary_key=True)
    # SellerName:Text(255) False
    seller_name = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'seller'


class RetailItems(models.Model):
    # ID:Long(4) False
    id = models.BigAutoField(primary_key=True)
    # Category:Text(255) False
    category = models.CharField(max_length=255, null=True)
    # No:Integer(2) False
    number = models.IntegerField(null=True)
    # DisplayName:Text(255) False
    display_name = models.CharField(max_length=255, null=True)
    # NormName:Text(255) False
    norm_name = models.CharField(max_length=255, null=True)
    # Price:Currency(8) False
    price = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    # Cost:Currency(8) False
    cost = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    # VATType:Text(255) False
    vat_type = models.CharField(max_length=255, null=True)
    # VATRate:Currency(8) False
    vat_rate = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    # 商品区分:Text(255) False
    product_category = models.CharField(max_length=255, null=True)
    # 仕入先名:Text(255) False
    supplier_name = models.CharField(max_length=255, null=True)
    # Seller:Long(4
    # Seller:Long(4) False
    seller = models.BigIntegerField(null=True)
    # Active:Boolean(1) False
    active = models.BooleanField(null=True)
    # RegistrationDate:Date/Time(8) False
    registration_date = models.DateTimeField(null=True)
    # UpdateDate:Date/Time(8) False
    update_date = models.DateTimeField(null=True)

    seller = models.ForeignKey(
        Seller, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'retail_items'


class Sales(models.Model):
    # Id:Long(4) False
    id = models.BigAutoField(primary_key=True)
    # SalesId:Text(255) False
    code = models.CharField(max_length=255, null=True)
    # Customer:Text(255) False
    customer = models.CharField(max_length=255, null=True)
    # From:Date/Time(8) False
    from_time = models.DateTimeField(null=True)
    # To:Date/Time(8) False
    to_time = models.DateTimeField(null=True)
    # GrossSalonSales:Currency(8) False
    gross_salon_sales = models.DecimalField(
        max_digits=19, decimal_places=2, null=True)
    # GrossRetailSales:Currency(8) False
    gross_retail_sales = models.DecimalField(
        max_digits=19, decimal_places=2, null=True)
    # TotalGrossSales:Currency(8) False
    total_gross_sales = models.DecimalField(
        max_digits=19, decimal_places=2, null=True)
    # TotalSalonDiscount:Currency(8) False
    total_salon_discount = models.DecimalField(
        max_digits=19, decimal_places=2, null=True)
    # RetailDiscount:Currency(8) False
    retail_discount = models.DecimalField(
        max_digits=19, decimal_places=2, null=True)
    # ServiceNetSales:Currency(8) False
    service_net_sales = models.DecimalField(
        max_digits=19, decimal_places=2, null=True)
    # RetailNetSales:Currency(8) False
    retail_net_sales = models.DecimalField(
        max_digits=19, decimal_places=2, null=True)
    # TotalNetSales:Currency(8) False
    total_net_sales = models.DecimalField(
        max_digits=19, decimal_places=2, null=True)
    # Cash:Currency(8) False
    cash = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    # Card:Currency(8) False
    card = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    # CardType:Text(255) False
    card_type = models.CharField(max_length=255, null=True)
    # EM:Currency(8) False
    em = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    # Prepaid:Currency(8) False
    prepaid = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    # Credit:Currency(8) False
    credit = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    # Tax:Currency(8) False
    tax = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    # Comment:Text(255) False
    comment = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'sales'


class SalesDetails(models.Model):
    # ID:Long(4) False
    id = models.BigAutoField(primary_key=True)
    # Customer:Text(255) False
    customer = models.CharField(max_length=255, null=True)
    # ItemType:Text(255) False
    item_type = models.CharField(max_length=255, null=True)
    # Staff:Text(255) False
    staff = models.CharField(max_length=255, null=True)
    # Amount:Integer(2) False
    amount = models.IntegerField(null=True)
    # Gross Sales:Currency(8) False
    gross_sales = models.DecimalField(
        max_digits=19, decimal_places=2, null=True)
    # Discount Type:Text(255) False
    discount_type = models.CharField(max_length=255, null=True)
    # Discount:Currency(8) False
    discount = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    # Net Sales:Currency(8) False
    net_sales = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    # フィールド1:Text(255) False
    field1 = models.CharField(max_length=255, null=True)
    # フィールド2:Text(255) False
    field2 = models.CharField(max_length=255, null=True)

    sale = models.ForeignKey(
        Sales, on_delete=models.SET_NULL, null=True, related_name='sales_details_sale')
    payment = models.ForeignKey(
        Sales, on_delete=models.SET_NULL, null=True, related_name='sales_details_payment')

    salon_item = models.OneToOneField(
        SalonItems, on_delete=models.SET_NULL, null=True, related_name='salon_item')
    retail_item = models.OneToOneField(
        RetailItems, on_delete=models.SET_NULL, null=True, related_name='retail_item')

    class Meta:
        db_table = 'sales_details'


class Hp(models.Model):
    # ID:Long(4) False
    id = models.BigAutoField(primary_key=True)
    # SalesDate:Date/Time(8) False
    sales_date = models.DateTimeField(null=True)
    # NetSales:Currency(8) False
    net_sales = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    # Points:Currency(8) False
    points = models.DecimalField(max_digits=19, decimal_places=2, null=True)

    sale = models.OneToOneField(
        Sales, on_delete=models.SET_NULL, null=True, related_name='hp')

    class Meta:
        db_table = 'hp'


class EmoneyType(models.Model):
    # ID:Long(4) False
    id = models.BigAutoField(primary_key=True)
    # 取引先:Text(255) False
    partner = models.CharField(max_length=255, null=True)
    # 品目:Text(255) False
    item = models.CharField(max_length=255, null=True)
    # TypeName:Text(255) False
    type_name = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'em_type'


class Emoney(models.Model):
    # Id:Long(4) False
    id = models.BigAutoField(primary_key=True)
    # 利用日付:Date/Time(8) False
    usage_date = models.DateTimeField(null=True)
    # 顧客名:Text(255) False
    customer_name = models.CharField(max_length=255, null=True)
    # 利用金額:Currency(8) False
    amount = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    # レジ担当:Text(255) False
    cashier = models.CharField(max_length=255, null=True)

    type = models.OneToOneField(
        EmoneyType, on_delete=models.SET_NULL, null=True, related_name='emoney_type')
    sale = models.ForeignKey(
        Sales, on_delete=models.SET_NULL, null=True, related_name='emoney')

    class Meta:
        db_table = 'e_money'


class Payments(models.Model):
    id = models.BigAutoField(primary_key=True)
    # Payment ID:Text(255) True
    payment_id = models.CharField(max_length=255)
    # Date:Date/Time(8) False
    date = models.DateTimeField(null=True)
    # Time:Date/Time(8) False
    time = models.DateTimeField(null=True)
    # Total Collected:Currency(8) False
    total_collected = models.DecimalField(
        max_digits=19, decimal_places=2, null=True)
    # Fees:Currency(8) False
    fees = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    # Net Total:Currency(8) False
    net_total = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    # Customer Name:Text(255) False
    customer_name = models.CharField(max_length=255, null=True)
    # Card Brand:Text(255) False
    card_brand = models.CharField(max_length=255, null=True)
    # PAN Suffix:Text(255) False
    pan_suffix = models.CharField(max_length=255, null=True)
    # Deposit Date:Text(255) False
    deposit_date = models.CharField(max_length=255, null=True)
    # Fee Percentage Rate:Currency(8) False
    fee_percentage_rate = models.DecimalField(
        max_digits=19, decimal_places=2, null=True)
    # フィールド1:Text(255) False
    field1 = models.CharField(max_length=255, null=True)

    sale = models.ForeignKey(
        Sales, on_delete=models.SET_NULL, null=True, related_name='sales_related')

    class Meta:
        db_table = 'payments'
