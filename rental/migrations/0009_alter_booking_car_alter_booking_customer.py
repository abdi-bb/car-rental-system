# Generated by Django 5.0 on 2023-12-24 21:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0008_remove_customer_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='car',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='rental.car'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rental.customer'),
        ),
    ]