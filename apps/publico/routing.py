from django.urls import path
from . import consumers  # Importa tu archivo de consumers

websocket_urlpatterns = [
    path("ws/fotos/", consumers.GalleryConsumer.as_asgi()),
    ]