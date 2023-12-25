# Generated by Django 5.0 on 2023-12-25 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0010_alter_car_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='status',
        ),
        migrations.AddField(
            model_name='car',
            name='availability',
            field=models.BooleanField(default=True),
        ),
    ]