# Generated by Django 4.1.7 on 2023-03-25 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales_management', '0005_rename_title_row_freeedeals_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='omron',
            old_name='gift_count',
            new_name='gift_ticket_quantity',
        ),
    ]
