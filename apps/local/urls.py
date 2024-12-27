from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

from apps.local import views as localViews


urlpatterns = [
    #DEF
    #path('subir_foto/<int:cod_evento>/', localViews.subir_fotoV3, name='subir_foto'),
    #FUNCIONES   
    #path('actualizar_ultima_foto/', photoeventViews.actualizar_ultima_foto, name='actualizar_ultima_foto'),           
    #VIEW
    #path('home', localViews.home.as_view(), name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
