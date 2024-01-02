from django.shortcuts import get_object_or_404, render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from customer.models import Customer

from .permissions import AdminCanNotPost
from .filters import BookingFilter
from booking.models import Booking
from .serializers import BookingSerializer


class BookingViewSet(ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [AdminCanNotPost, IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_staff:
                return Booking.objects.all()
            
            (customer_id, created) = Customer.objects.only('id').get_or_create(user_id=user.id)
            return Booking.objects.filter(customer_id=customer_id)
        else:
            return Booking.objects.none()
        
            # return super().get_queryset()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['user_id']
    filterset_class = BookingFilter
    search_fields = ['start_date', 'end_date' ]
    ordering_fields = ['start_date', 'end_date']
    
    def perform_create(self, serializer):
        user = self.request.user
        if user.is_authenticated and not user.is_staff:
            customer, created = Customer.objects.get_or_create(user=user)
            serializer.save(customer=customer)
        else:
            serializer.save()
    
    def destroy(self, request, *args, **kwargs):
        if Customer.objects.filter(booking__id=kwargs['pk']).count() > 0:
            return Response({'error': 'Booking can not be deleted because there is associated Customer with it.'})

        return super().destroy(request, *args, **kwargs)
