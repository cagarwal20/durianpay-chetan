from rest_framework import serializers
from .models import Product
class ProductSerializer(serializers.ModelSerializer):
    is_second_hand_included = serializers.SerializerMethodField()

    def get_is_second_hand_included(self,obj):
        return False
    
    class Meta:
        model = Product
        fields = '__all__'

class ProductPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['url','website','title','price']