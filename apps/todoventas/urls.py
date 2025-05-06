from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from apps.todoventas import views as todoventasViews


urlpatterns = [
    #DEF
    #VIEW
    path('todoventas/home/', todoventasViews.homeTodoVentasView.as_view(), name='todoventas'),
    path('todoventas/lista_productos/', todoventasViews.listaProductosView.as_view(), name='todoventas-lista-productos'),     
    path('todoventas/gestion_categorias/', todoventasViews.listaCategoriasView.as_view(), name='todoventas-gestion_categorias'),
    path('todoventas/gestion_ventas/', todoventasViews.gestionVentasView.as_view(), name='todoventas-gestion_ventas'),
    # --------------------------------------------DEF AMBV------------------------------------------------------------------
    path('nuevo_registro/', todoventasViews.nuevo_registro, name='nuevo_registro'),    
    path('obtener_registro/', todoventasViews.obtener_registro, name='obtener_registro'),   
    path('actualizar_registro/', todoventasViews.actualizar_registro, name='actualizar_registro'),  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
