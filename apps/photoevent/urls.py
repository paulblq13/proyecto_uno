from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

from apps.photoevent import views as photoeventViews


urlpatterns = [
    #DEF
    path('subir_foto/<int:cod_evento>/', photoeventViews.subir_fotoV3, name='subir_foto'),
    path('moderar_fotos/<int:cod_evento>/', photoeventViews.moderar_fotos, name='moderar_fotos'),
    path('galeria_fotos/<int:cod_evento>/', photoeventViews.GaleriaFotosView.as_view(), name="galeria_fotos"), 
    path('ingresar_codigo/', views.ingresar_codigo, name='ingresar_codigo'),
    
    #FUNCIONES   
    #path('actualizar_ultima_foto/', photoeventViews.actualizar_ultima_foto, name='actualizar_ultima_foto'),           
    #VIEW
    path('galeria/<int:cod_evento>/<int:index>/', photoeventViews.LiveGaleriaView.as_view(), name='galeria'),
    path('galeria/<int:cod_evento>/', photoeventViews.LiveGaleriaView.as_view(), name='galeria'),
    path('photoevent/lista/', photoeventViews.PhotoEventListaView.as_view(), name='photoevent-lista'),
    path('photoevent/agregar/', photoeventViews.addEventoView.as_view(), name="photoevent-agregar"),     
    path('photoevent/modificar/<int:pk>/', photoeventViews.updateEventoView.as_view(), name="photoevent-modificar"),   
    path('photoevent/detalle/<int:pk>/', photoeventViews.detallesEventoView.as_view(), name="photoevent-detalle"),     

    path('galeria2/<int:cod_evento>/<int:index>/', photoeventViews.LiveGaleriaView2.as_view(), name='galeria2'),
    path('galeria2/<int:cod_evento>/', photoeventViews.LiveGaleriaView2.as_view(), name='galeria2'),     
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
