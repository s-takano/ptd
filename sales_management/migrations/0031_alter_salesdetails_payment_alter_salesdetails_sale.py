# Generated by Django 4.1.7 on 2023-03-28 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales_management', '0030_alter_payments_deposit_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesdetails',
            name='payment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payment_details', to='sales_management.sales'),
        ),
        migrations.AlterField(
            model_name='salesdetails',
            name='sale',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='details', to='sales_management.sales'),
        ),
    ]