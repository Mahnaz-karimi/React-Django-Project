from django.shortcuts import render
from rest_framework import generics, status # generic.ListAPIVIEW allowed us to create a class inherits from a generic API view # status for access to http status code when we use Response
from .serializers import RoomSerializer, CreateRoomSerializer
from api.models import Room
from rest_framework.views import APIView
from rest_framework.response import Response # get response from our view

# Create your views here.


class RoomView(generics.ListAPIView): # Is a already set up to return to us all of difference room  
    queryset = Room.objects.all() 
    serializer_class = RoomSerializer


class CreateRoomView(APIView): # APIView allowed us to overwrite default ( get and post )method 
    serializer_class = CreateRoomSerializer

    def post(self, request, format=None): 
        if not self.request.session.exists(self.request.session.session_key): # For at identify host we should use session-key.# Session is a temporary connection between to computer or devices
            self.request.session.create() # if there is no session so makes a session

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(): # if there are those data, that should to be like 'guest_can_pause', 'votes_to_skip'
            guest_can_pause = serializer.data.get('guest_can_pause') # get they data
            votes_to_skip = serializer.data.get('votes_to_skip')
            host = self.request.session.session_key
            queryset = Room.objects.filter(host=host)  
            if queryset.exists(): # If there is any room with the same host code
                room = queryset[0] # get det first room
                room.guest_can_pause = guest_can_pause
                room.votes_to_skip = votes_to_skip
                room.save(update_fields=['guest_can_pause', 'votes_to_skip'])
                return Response(RoomSerializer(room).data, status=status.HTTP_200_OK)
            else: # If there is any room so makes a room 
                room = Room(host=host, guest_can_pause=guest_can_pause,
                            votes_to_skip=votes_to_skip)
                room.save()
                return Response(RoomSerializer(room).data, status=status.HTTP_201_CREATED) # serilize the room

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)