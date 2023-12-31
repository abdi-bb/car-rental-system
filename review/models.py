from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from car.models import Car
from user.models import User

# Create your models here.
    
class Review(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='reviews')
    description = models.TextField()
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),
                                                    MaxValueValidator(5)])
    
    def __str__(self):
        return f"Review ID: {self.id} - {self.user.username} on {self.car.name}"
