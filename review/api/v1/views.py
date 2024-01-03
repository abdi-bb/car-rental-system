from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.core.validators import ValidationError
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers

from car.models import Car

from .permissions import AdminCanNotPost, CanModifyOwnReview, IsAdminOrReadOnly
from review.models import Review
from .serializers import ReviewSerializer


class ReviewViewSet(ModelViewSet):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, CanModifyOwnReview]
    
    def perform_create(self, serializer):
        car_pk = self.kwargs.get("car_pk")
        car = get_object_or_404(Car, pk=car_pk)
        
        user = self.request.user
        review_queryset = Review.objects.filter(car=car,
                                                user=user.id)
        
        if review_queryset.exists():
            raise serializers.ValidationError("You have already reviewed this car!")
        # Set the user field to the current authenticated user's user instance
        serializer.save(user=self.request.user)
        
    def get_queryset(self):
        return Review.objects.filter(car_id=self.kwargs.get('car_pk'))
        # return super().get_queryset()
    
    def get_serializer_context(self):
        return {'car_id': self.kwargs.get('car_pk')}