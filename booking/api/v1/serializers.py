from rest_framework import serializers

from car.api.v1.serializers import CarSerializer
from user.api.v1.serializers import UserSerializer


from booking.models import Booking



class BookingSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(source='user.id', read_only=True)
    car = CarSerializer
    class Meta:
        model = Booking
        fields = ['id',  'car', 'user_id', 'start_date', 'end_date', 'total_price']
    # user = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    # car = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all())
    # user = UserSerializer()
    # car = CarSerializer()
    # user = serializers.HyperlinkedRelatedField(
    #     queryset=Customer.objects.all(),
    #     view_name='user-detail'
    # )
    # car = serializers.HyperlinkedRelatedField(
    #     queryset=Car.objects.all(),
    #     view_name='car-detail'
    # )
    
    total_price = serializers.SerializerMethodField(method_name='calculate_total_price')
    
    def calculate_total_price(self, car):
        pass
    
