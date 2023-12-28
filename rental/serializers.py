from django.utils import timezone
from rest_framework import serializers
from accounts.serializers import CustomerSerializer


from rental.models import Booking, Car, CarImage, Review, Customer

    
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
    class Meta:
        model = Car
        fields = ['id', 'name', 'model', 'seat', 'door', 'gearbox', 'price', 'images']

        



class BookingSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    car = CarSerializer
    class Meta:
        model = Booking
        fields = ['id', 'start_date', 'end_date', 'customer', 'car', 'total_price']
    # customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    # car = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all())
    # customer = CustomerSerializer()
    # car = CarSerializer()
    # customer = serializers.HyperlinkedRelatedField(
    #     queryset=Customer.objects.all(),
    #     view_name='customer-detail'
    # )
    # car = serializers.HyperlinkedRelatedField(
    #     queryset=Car.objects.all(),
    #     view_name='car-detail'
    # )
    
    total_price = serializers.SerializerMethodField(method_name='calculate_total_price')
    
    def calculate_total_price(self, car):
        pass
    
    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'customer_id', 'name', 'date', 'description']
        
    def create(self, validated_data):
        car_id = self.context['car_id']
        return Review.objects.create(car_id=car_id, **validated_data)
        # return super().create(validated_data)
