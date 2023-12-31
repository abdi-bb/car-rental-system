from django.db import models


class Car(models.Model):
    MANUAL = 'M'
    AUTOMATIC = 'A'
    GEARBOX_CHOICES = [(MANUAL, 'Manual'), (AUTOMATIC, 'Automatic')]
    
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    availabile = models.BooleanField(default=True)
    seat = models.PositiveIntegerField()
    door = models.PositiveIntegerField()
    gearbox = models.CharField(max_length=1, choices=GEARBOX_CHOICES)
    # image = models.ImageField(upload_to='rental/cars/images', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.name} ({self.model})"
    
    
class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='rental/cars/images', null=True, blank=True)
