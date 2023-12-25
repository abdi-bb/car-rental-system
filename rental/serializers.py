from django.utils import timezone
from rest_framework import serializers

from rental.models import Booking, Car, Review, Customer


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'name', 'model', 'seat', 'door', 'gearbox', 'image', 'price']
    
    
class CustomerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    
    class Meta:
        model = Customer
        fields = ['id', 'user_id', 'first_name', 'last_name', 'phone_number', 'email']
    

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'start_date', 'end_date', 'customer', 'car', 'total_price']
    # customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    # car = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all())
    # customer = CustomerSerializer()
    # car = CarSerializer()
    customer = serializers.HyperlinkedRelatedField(
        queryset=Customer.objects.all(),
        view_name='customer-detail'
    )
    car = serializers.HyperlinkedRelatedField(
        queryset=Car.objects.all(),
        view_name='car-detail'
    )
    total_price = serializers.SerializerMethodField(method_name='calculate_total_price')
    
    def calculate_total_price(self, car):
        pass
    
    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'date', 'name', 'description']
        
    def create(self, validated_data):
        car_id = self.context['car_id']
        return Review.objects.create(car_id=car_id, **validated_data)
        # return super().create(validated_data)