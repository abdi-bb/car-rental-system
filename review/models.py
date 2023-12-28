from django.db import models
from car.models import Car

from customer.models import Customer

# Create your models here.
    
class Review(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='reviews')
    # name = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return f"Review ID: {self.id} - {self.customer.username} on {self.car.name}"
