from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated

class UserList(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = (TokenAuthentication,) 
    queryset = User.objects.all()
    serializer_class = UserSerializer