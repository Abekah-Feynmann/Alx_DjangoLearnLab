from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import response
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate




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

        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]

            #checks if user exists and creates a user object if authentication check is run successfully
            user = authenticate(username=username, password=password)
        return Response(serializer.errors, status=400)
        
        #Generate token based on the existence of a user
        if user is None:
            return Response({"error" : "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        token, created = Token.objects.get_or_create(user=user)

        return Response({"message" : "Login Successful"}, {"token" : token.key})  

#creating the profile view
class ProfileView(APIView):
    def post(self, request):
        serializer = LoginSerializer(user=request.user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Profile updated successfully",
                            "data" = serializer.data}, status = status.HTTP_200_OK                
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




