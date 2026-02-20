from .models import CustomUser
from rest_framework import serializers
from django.contrib.auth import get_user_model

#Create serializers for CustomUser model
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

"""
    Create serializers for registeration
"""
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={"Input_type: password"})
    password2 =  serializers.CharField(write_only=True, required=True, style={"Input_type: password"})

    class Meta:
        model = CustomUser
        fields = '__all__'

    #validating the data
    def validate(self, data):
        if data['password'] != data['password2']:
            return serializers.ValidationError("Password: Passwords do not match")
        return data

    #creating the user
    def create(self, validated_data):
        validated_data.pop('password2')

        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data.get("email"),
            password = validated_data['password']
        )

        return user


"""
    Creating the serializer for login
"""

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


"""
    Creating the serializer for Profile
"""

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)
    class Meta:
        model = CustomUser
        fields = ["id", "profile_picture,", "bio", "followers"]





