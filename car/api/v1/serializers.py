from rest_framework import serializers

from car.models import Car, CarImage

    
class CarImageSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        car_id = self.context['car_id']
        return CarImage.objects.create(car_id=car_id, **validated_data)
        # return super().create(validated_data)
        
    class Meta:
        model = CarImage
        fields = ['id', 'image']

class CarSerializer(serializers.ModelSerializer):
    images = CarImageSerializer(many=True, read_only=True)
    class Meta:
        model = Car
        fields = ['id', 'name', 'model', 'seat', 'door', 'gearbox', 'price', 'images']

