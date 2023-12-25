from django.shortcuts import get_object_or_404, render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from .permissions import CanViewReviewDetail, IsAdminOrReadOnly
from .filters import BookingFilter, CarFilter
from .models import Booking, Car, Review, Customer
from .serializers import BookingSerializer, CarSerializer, ReviewSerializer, CustomerSerializer


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAdminOrReadOnly]
    
    def get_serializer_context(self):
        return {'request': self.request}
    
    def destroy(self, request, *args, **kwargs):
        if Booking.objects.filter(car_id=kwargs['pk']).count() > 0:
            return Response({'error': "Car can not be deleted because there is a booking tied to it."})
        
        return super().destroy(request, *args, **kwargs)
    

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser]
    
    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        (customer, created) = Customer.objects.get_or_create(user_id=request.user.id)
        if request.method == 'GET':
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = CustomerSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        

class BookingViewSet(ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Booking.objects.all()
        
        (customer_id, created) = Customer.objects.only('id').get_or_create(user_id=user.id)
        return Booking.objects.filter(customer_id=customer_id)
        # return super().get_queryset()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['user_id']
    filterset_class = BookingFilter
    search_fields = ['start_date', 'end_date' ]
    ordering_fields = ['start_date', 'end_date']
    
    def destroy(self, request, *args, **kwargs):
        if Customer.objects.filter(booking__id=kwargs['pk']).count() > 0:
            return Response({'error': 'Booking can not be deleted because there is associated user with it.'})

        return super().destroy(request, *args, **kwargs)


class ReviewViewSet(ModelViewSet):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [CanViewReviewDetail | IsAdminOrReadOnly]
    
    def perform_create(self, serializer):
        # Set the customer field to the current authenticated user's customer instance
        serializer.save(customer=self.request.user.customer)
        
    def get_queryset(self):
        return Review.objects.filter(car_id=self.kwargs['car_pk'])
        # return super().get_queryset()
    
    def get_serializer_context(self):
        return {'car_id': self.kwargs['car_pk']}