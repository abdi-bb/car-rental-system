# Generated by Django 5.0 on 2023-12-25 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0009_alter_booking_car_alter_booking_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]