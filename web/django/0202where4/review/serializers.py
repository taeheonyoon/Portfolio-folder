from rest_framework.serializers import ModelSerializer
from .models import Store, Review

class StoreSerializer(ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'
        
class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'