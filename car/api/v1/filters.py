from django_filters.rest_framework import FilterSet
from car.models import Car

class CarFilter(FilterSet):
    # class Meta:
    #     model = Car
    #     fields = {
    #         'booking_id': ['exact'],
    #         'price': ['gt', 'lt']
    #     }
    pass
