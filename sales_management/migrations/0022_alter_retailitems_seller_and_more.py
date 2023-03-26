# Generated by Django 4.1.7 on 2023-03-26 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales_management', '0021_alter_emoney_sale_alter_emoney_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retailitems',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sales_management.seller'),
        ),
        migrations.AlterField(
            model_name='salesdetails',
            name='retail_item',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='retail_item', to='sales_management.retailitems'),
        ),
        migrations.AlterField(
            model_name='salesdetails',
            name='salon_item',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='salon_item', to='sales_management.salonitems'),
        ),
    ]
