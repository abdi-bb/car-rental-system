from django.db import migrations, models
import datetime

def convert_date_to_datetime(apps, schema_editor):
    Review = apps.get_model('rental', 'Review')
    for review in Review.objects.all():
        # Convert the date field to a datetime value
        review.date = datetime.datetime.combine(review.date, datetime.time.min)
        review.save()

class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0016_alter_review_customer_alter_booking_customer_and_more'),
    ]

    operations = [
        migrations.RunPython(convert_date_to_datetime),
    ]
