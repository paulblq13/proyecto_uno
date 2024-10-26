from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

from apps.photoevent import views as photoeventViews


urlpatterns = [
    #DEF
    path('subir_foto/', photoeventViews.subir_foto, name='subir_foto'),    
    path('moderar_fotos/', photoeventViews.moderar_fotos, name='moderar_fotos'),
    path('lista_fotos_aprobadas/', photoeventViews.UltimaFotoView.as_view(), name="lista_fotos_aprobadas"),       
    #VIEW

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
