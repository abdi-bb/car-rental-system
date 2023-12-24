from django_filters.rest_framework import FilterSet
from .models import Booking, Car

class CarFilter(FilterSet):
    # class Meta:
    #     model = Car
    #     fields = {
    #         'booking_id': ['exact'],
    #         'price': ['gt', 'lt']
    #     }
    pass

     
class UserFilter(FilterSet):
    pass


class BookingFilter(FilterSet):
    class Meta:
        model = Booking
        fields = {
            'customer_id': ['exact'],
            'end_date': ['gt', 'lt']
        }