# Generated by Django 4.1.7 on 2023-03-29 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales_management', '0032_rename_emoneytype_emoneytypes_rename_hp_hps_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hps',
            name='sale',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hps', to='sales_management.sales'),
        ),
    ]
