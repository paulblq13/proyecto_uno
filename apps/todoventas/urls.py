from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from apps.todoventas import views as todoventasViews


urlpatterns = [
    #DEF
    #VIEW
    path('todoventas/home/', todoventasViews.homeTodoVentasView.as_view(), name='todoventas'),    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
