from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token





# Create your views here.

#Creating a registration view
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data= request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "user registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# creating the login view
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=200)


#creating the profile view
class ProfileView(APIView):
    def post(self, request):
        serializer = LoginSerializer(user=request.user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Profile updated successfully",
                            "data": serializer.data}, status = status.HTTP_200_OK                
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




