# Generated by Django 4.1.7 on 2023-03-28 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_management', '0029_alter_payments_deposit_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='deposit_date',
            field=models.DateTimeField(null=True),
        ),
    ]