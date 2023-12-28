from django.shortcuts import get_object_or_404, render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from .permissions import AdminCanNotPost, CanModifyOwnReview, IsAdminOrReadOnly
from review.models import Review
from .serializers import ReviewSerializer


class ReviewViewSet(ModelViewSet):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [AdminCanNotPost | CanModifyOwnReview | IsAdminOrReadOnly]
    
    def perform_create(self, serializer):
        # Set the customer field to the current authenticated user's customer instance
        serializer.save(customer=self.request.user.customer)
        
    def get_queryset(self):
        return Review.objects.filter(car_id=self.kwargs['car_pk'])
        # return super().get_queryset()
    
    def get_serializer_context(self):
        return {'car_id': self.kwargs['car_pk']}