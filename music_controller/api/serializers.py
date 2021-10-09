from rest_framework import serializers
from .models import Room


class RoomSerializer(serializers.ModelSerializer): # Get all this field in room classe from database 
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause',
                  'votes_to_skip', 'created_at')

class CreateRoomSerializer(serializers.ModelSerializer): # For at se these variable is on the http post request is valid & enough for make a room 
    class Meta:
        model = Room
        fields = ('guest_can_pause', 'votes_to_skip') # when is sendign a post request, has this payload: 'guest_can_pause', 'votes_to_skip'