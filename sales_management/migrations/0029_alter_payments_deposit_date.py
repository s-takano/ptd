# Generated by Django 4.1.7 on 2023-03-28 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_management', '0028_alter_payments_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='deposit_date',
            field=models.DateField(null=True),
        ),
    ]
