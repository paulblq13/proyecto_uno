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
    path('actualizar_ultima_foto/', photoeventViews.actualizar_ultima_foto, name='actualizar_ultima_foto'),           
    #VIEW
    path('galeria/<int:index>/', photoeventViews.UltimaFotoView.as_view(), name='galeria_aprobada'),
    path('galeria/', photoeventViews.UltimaFotoView.as_view(), name='galeria_aprobada'),    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
