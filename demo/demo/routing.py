from django.urls import path, re_path
from myapp import consumers

websocket_urlpatterns = [
    re_path('ws/some_path/', consumers.YourConsumer.as_asgi()),
]