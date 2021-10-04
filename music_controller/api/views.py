from django.shortcuts import render
from rest_framework import generics # generic.ListAPIVIEW allowed us to create a class inherits from a generic API view
from .serializers import RoomSerializer
from api.models import Room

# Create your views here.


class RoomView(generics.ListAPIView): # is a already set up to return to us all of difference room  
    queryset = Room.objects.all() 
    serializer_class = RoomSerializer

