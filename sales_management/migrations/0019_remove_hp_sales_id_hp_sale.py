# Generated by Django 4.1.7 on 2023-03-26 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales_management', '0018_alter_emoney_sale_alter_salesdetails_sale'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hp',
            name='sales_id',
        ),
        migrations.AddField(
            model_name='hp',
            name='sale',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sales_management.sales'),
        ),
    ]
