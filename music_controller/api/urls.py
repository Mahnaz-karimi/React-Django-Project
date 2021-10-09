from django.urls import path
from .views import RoomView, CreateRoomView

urlpatterns = [
    path('room', RoomView.as_view(), name='room'),
    path('create-room', CreateRoomView.as_view()),
]