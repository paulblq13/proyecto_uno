from django.urls import re_path
from ..apps.publico import consumers

websocket_urlpatterns = [
    re_path(r'ws/media/$', consumers.GalleryConsumer.as_asgi()),
]