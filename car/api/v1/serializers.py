from rest_framework import serializers
from car.api.v1.utils import calculate_average_rating

from car.models import Car, CarImage
from review.api.v1.serializers import ReviewSerializer

    
class CarImageSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        car_id = self.context['car_id']
        return CarImage.objects.create(car_id=car_id, **validated_data)
        # return super().create(validated_data)
        
    class Meta:
        model = CarImage
        fields = ['id', 'image']
        

class CarSerializer(serializers.ModelSerializer):
    images = CarImageSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()
    class Meta:
        model = Car
        fields = ['id', 'name', 'model', 'seat', 'door', 'gearbox', 'price', 'images', 'reviews', 'average_rating']
        
    def get_average_rating(self, obj):
        reviews = list(obj.reviews.all())
        return calculate_average_rating(reviews)

