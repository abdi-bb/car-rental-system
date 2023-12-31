from rest_framework import serializers

from review.models import Review
    
    
class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.StringRelatedField(source='user.username', read_only=True)
    car_name = serializers.StringRelatedField(source='car.name', read_only=True)
    class Meta:
        model = Review
        fields = ['id', 'user_id', 'username', 'car_id', 'car_name', 'description', 'created_at', 'updated_at', 'rating']
        
    def create(self, validated_data):
        car_id = self.context['car_id']
        return Review.objects.create(car_id=car_id, **validated_data)
        # return super().create(validated_data)
