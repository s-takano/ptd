# Generated by Django 4.1.7 on 2023-03-26 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_management', '0008_remove_sales_sales_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='id',
            field=models.BigAutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='payments',
            name='payment_id',
            field=models.CharField(max_length=255),
        ),
    ]
