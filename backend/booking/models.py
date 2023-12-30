from django.db import models
from django.forms import ValidationError
from django.utils import timezone

from customer.models import Customer
from car.models import Car

# Create your models here.


class Booking(models.Model):
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    car = models.OneToOneField(Car, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"Booking ID: {self.id} - {self.car.name} ({self.start_date} to {self.end_date})"
    
    def clean(self):
        # Check for overlapping bookings for the same car
        overlapping_bookings = Booking.objects.filter(
            car=self.car,
            end_date__gte=self.start_date,
            start_date__lte=self.end_date
        ).exclude(pk=self.pk)  # Exclude the current booking if it's an update
        if overlapping_bookings.exists():
            raise ValidationError("This car is already booked for the specified time period.")

    def save(self, *args, **kwargs):
        self.clean()  # Perform the validation before saving
        super().save(*args, **kwargs)
 