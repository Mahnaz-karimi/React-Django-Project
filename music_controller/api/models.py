from django.db import models
import string
import random


def generate_unique_code(): # make a unique number for every room that use for sende request for come in the room
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length)) # finde a code with UPPERCASE string and length 6
        if Room.objects.filter(code=code).count() == 0: # if there is a room with det same code, makes a new code,             
            break # until it can generate a unique code and breaks while-loop

    return code


# Create models here, and you can put most of logics on models-page for make a good models
class Room(models.Model):
    code = models.CharField(max_length=8, default=generate_unique_code, unique=True) # every time make a new room call the generate_unique_code's method (with out any brackets)
    host = models.CharField(max_length=50, unique=True) # Every room have only one host. For at identify host we should use session-key.# Session is a temporary connection between to computer or devices
    guest_can_pause = models.BooleanField(null=False, default=False) 
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
