from .models import CustomUser
from rest_framework import serializers

#Create serializers for CustomUser model
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'