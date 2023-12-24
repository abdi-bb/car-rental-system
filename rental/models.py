from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Car(models.Model):
    MANUAL = 'M'
    AUTOMATIC = 'A'
    GEARBOX_CHOICES = [(MANUAL, 'Manual'), (AUTOMATIC, 'Automatic')]
    
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    seat = models.PositiveIntegerField()
    door = models.PositiveIntegerField()
    gearbox = models.CharField(max_length=1, choices=GEARBOX_CHOICES)
    image = models.ImageField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Customer(models.Model):
    phone_number = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Booking(models.Model):
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    car = models.OneToOneField(Car, on_delete=models.PROTECT)
    
class Review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
