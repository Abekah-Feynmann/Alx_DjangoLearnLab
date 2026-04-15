from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework import status, generics, permissions
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .models import CustomUser
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType






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
        serializer = ProfileSerializer(user=request.user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Profile updated successfully",
                            "data": serializer.data}, status = status.HTTP_200_OK                
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#creating a view for following a user
class FollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        target_user = self.get_object()

        if request.user == target_user:
            return Response({"Error": "You cannot follow yourself"},
                             status = status.HTTP_400_BAD_REQUEST)
        
        request.user.following.add(target_user)
        Notification.objects.create(
            recipient = target_user,
            actor = request.user,
            verb = f"{request.user} started following you!",
            content_type = ContentType.objects.get_for_model(target_user),
            object_id = target_user.id,
            timestamp = timezone.now()
        )
        return Response({"message": "Followed successfully"}, 
                        status = status.HTTP_200_OK)

#Creating a view for unfollowing a user
class UnFollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        target_user = self.get_object()
        
        request.user.following.remove(target_user)
        return Response({"message": "Unfollowed successfully"},
                        status = status.HTTP_200_OK)



