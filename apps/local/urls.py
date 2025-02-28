from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

from apps.local import views as localViews


urlpatterns = [
    #DEF
    path('api/articulos/', localViews.search_articulos, name='search_articulos'),
    #path('subir_foto/<int:cod_evento>/', localViews.subir_fotoV3, name='subir_foto'),
    #FUNCIONES   
    #path('actualizar_ultima_foto/', photoeventViews.actualizar_ultima_foto, name='actualizar_ultima_foto'),           
    #VIEW
    #path('home', localViews.home.as_view(), name='home'),
    path('local/home/', localViews.homeLocalView.as_view(), name="local-home"), 

    path('local/lista-productos/', localViews.productosView.as_view(), name="lista-productos"),
    path('local/lista-ventas/', localViews.listaVentasView.as_view(), name="lista-ventas"),

    path('local/agregar-articulo/', localViews.addArticuloView.as_view(), name="agregar-articulo"),
    path('local/agregar-venta/', localViews.addVentaView.as_view(), name="agregar-venta"),    

    path('local/modificar-articulo/<int:pk>/', localViews.updateArticuloView.as_view(), name="modificar-articulo"),    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
