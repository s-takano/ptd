# Generated by Django 4.1.7 on 2023-03-26 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales_management', '0024_alter_salesdetails_retail_item_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesdetails',
            name='retail_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='salon_details', to='sales_management.retailitems'),
        ),
        migrations.AlterField(
            model_name='salesdetails',
            name='salon_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='salon_details', to='sales_management.salonitems'),
        ),
    ]
