from django.urls import path
from .consumers import ChatroomConsumer
from django.urls import re_path

websocket_urlpatterns = [
    path("ws/chatroom/<chatroom_name>/", ChatroomConsumer.as_asgi()),
]