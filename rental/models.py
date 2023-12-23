from django.db import models
from django.utils import timezone

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    seat = models.PositiveIntegerField()
    door = models.PositiveIntegerField()
    gearbox = models.CharField(max_length=255)
    image = models.BinaryField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class User(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.PositiveIntegerField(default=0)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.OneToOneField(Car, on_delete=models.CASCADE)
    start_date = models.DateField(default=None, blank=True, null=True)
    end_date = models.DateField()

    def save(self, *args, **kwargs):
        # If start_date is not provided, set it to the current date
        if not self.start_date:
            self.start_date = timezone.now().date()

        super().save(*args, **kwargs)

