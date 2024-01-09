from django.db import models
from django.forms import ValidationError
from django.utils import timezone

from user.models import User
from car.models import Car

# Create your models here.


class Booking(models.Model):
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    car = models.OneToOneField(Car, on_delete=models.PROTECT)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.car.availabile = 0
        self.car.save()
    
    def __str__(self):
        return f"Booking ID: {self.id} - {self.car.name} ({self.start_date} to {self.end_date})"
 