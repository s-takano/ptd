# Generated by Django 4.1.7 on 2023-03-25 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales_management', '0003_rename_emtype_emoneytype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emoney',
            old_name='usage_amount',
            new_name='amount',
        ),
    ]
