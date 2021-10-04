from django.db import models
import string
import random


def generate_unique_code(): # make a unique number for every room that use for sende request for come in the room
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length)) # finde a code with UPPERCASE string and length 6
        if Room.objects.filter(code=code).count() == 0: # if there is a room with det same code, makes a new code,             
            break # until it can make unique code

    return code


# Create models here, and you can put most of logics on models for make a good models


class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=50, unique=True) # every room have only one host
    guest_can_pause = models.BooleanField(null=False, default=False) 
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
