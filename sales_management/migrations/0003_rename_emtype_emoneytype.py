# Generated by Django 4.1.7 on 2023-03-25 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales_management', '0002_rename_saller_seller_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EMType',
            new_name='EMoneyType',
        ),
    ]
