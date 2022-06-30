from .serializers import UserSerializer, RegisterSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,  IsAdminUser, Allow_any
from rest_framework_simplejwt.authentication import JWTAuthentication

# user data api


class UserData(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

# user registration api


class RegisterUserAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [Allow_any]
