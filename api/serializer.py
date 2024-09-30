from .models import Company,
from rest_framework.serializers import ModelSerializer

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class HotelSerializer(ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'