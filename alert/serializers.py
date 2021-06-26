from rest_framework import serializers
from .models import *



class MerchantSerializer(serializers.ModelSerializer): # merchant serializer
    class Meta:
        fields = '__all__'
        model = Merchant
