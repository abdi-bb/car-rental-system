from django.shortcuts import get_object_or_404, render

# Create your views here.
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers

from booking.models import Booking

from .permissions import IsAdminOrReadOnly
from car.models import Car, CarImage
from .serializers import CarImageSerializer, CarSerializer


class CarViewSet(ModelViewSet):
    queryset = Car.objects.prefetch_related('images').all()
    serializer_class = CarSerializer
    permission_classes = [IsAdminOrReadOnly]
    
    def get_serializer_context(self):
        return {'request': self.request}
    
    def destroy(self, request, *args, **kwargs):
        if Booking.objects.filter(car_id=kwargs['pk']).count() > 0:
            raise serializers.ValidationError("Car can not be deleted because there is a booking tied to it.")
        return super().destroy(request, *args, **kwargs)


class CarImageViewSet(ModelViewSet):
    serializer_class = CarImageSerializer
    permission_classes = [IsAdminOrReadOnly]
    
    def get_serializer_context(self):
        return {'car_id': self.kwargs.get('car_pk')}
        # return super().get_serializer_context()
    
    def get_queryset(self):
        return CarImage.objects.filter(car_id=self.kwargs.get('car_pk'))
        # return super().get_queryset()