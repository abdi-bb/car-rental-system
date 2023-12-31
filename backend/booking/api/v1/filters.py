from django_filters.rest_framework import FilterSet
from booking.models import Booking

class BookingFilter(FilterSet):
    class Meta:
        model = Booking
        fields = {
            'customer_id': ['exact'],
            'end_date': ['gt', 'lt']
        }