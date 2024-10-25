from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import apps.publico.routing  # Importa las rutas de WebSocket de la app publico
from django.core.asgi import get_asgi_application

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            apps.publico.routing.websocket_urlpatterns  # Usa las rutas de WebSocket de publico
        )
    ),
})