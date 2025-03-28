from django.urls import path
from . import views  # Importa tus vistas desde el mismo módulo
from apps.publico import views as publicoViews

urlpatterns = [
    #DEF
    #VIEW
    path('serexv1/', publicoViews.Invitacion01View.as_view(), name='invitacion01'),        
    path('invitacion02/', publicoViews.Invitacion02View.as_view(), name='invitacion02'), 
    path('invitacion03/', publicoViews.Invitacion03View.as_view(), name='invitacion03'),       
    path('subirfoto/', views.upload_photo, name='subirfoto'),
    path('media/', views.photo_gallery, name='media'),    
]
