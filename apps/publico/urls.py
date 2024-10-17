from django.urls import path
from . import views  # Importa tus vistas desde el mismo módulo
from apps.publico import views as publicoViews

urlpatterns = [
    #DEF
    #VIEW
    path('invitacion01', publicoViews.Invitacion01View.as_view(), name='invitacion01'),        
    path('invitacion02', publicoViews.Invitacion02View.as_view(), name='invitacion02'), 
    path('invitacion03', publicoViews.Invitacion03View.as_view(), name='invitacion03'),       
    
]
