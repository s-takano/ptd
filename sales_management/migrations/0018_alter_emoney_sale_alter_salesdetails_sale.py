# Generated by Django 4.1.7 on 2023-03-26 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales_management', '0017_remove_emoney_sales_id_remove_emoney_type_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emoney',
            name='sale',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sales_emoney', to='sales_management.sales'),
        ),
        migrations.AlterField(
            model_name='salesdetails',
            name='sale',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sales_details_sale', to='sales_management.sales'),
        ),
    ]
