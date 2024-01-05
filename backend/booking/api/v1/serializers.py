from rest_framework import serializers

from car.api.v1.serializers import CarSerializer
from customer.api.v1.serializers import CustomerSerializer


from booking.models import Booking



class BookingSerializer(serializers.ModelSerializer):
    # customer = CustomerSerializer(read_only=True)
    customer_id = serializers.PrimaryKeyRelatedField(source='customer.id', read_only=True)
    car = CarSerializer
    class Meta:
        model = Booking
        fields = ['id',  'car', 'customer_id', 'start_date', 'end_date', 'total_price']
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
    
