# Generated by Django 5.0 on 2023-12-23 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0002_alter_car_gearbox_reviews'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reviews',
            new_name='Review',
        ),
    ]