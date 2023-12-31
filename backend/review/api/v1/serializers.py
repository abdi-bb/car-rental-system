from rest_framework import serializers

from review.models import Review
    
    
class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.StringRelatedField(source='customer.user.username', read_only=True)
    class Meta:
        model = Review
        fields = ['id', 'customer_id', 'username', 'description', 'created_at', 'updated_at', 'rating']
        
    def create(self, validated_data):
        car_id = self.context['car_id']
        return Review.objects.create(car_id=car_id, **validated_data)
        # return super().create(validated_data)
