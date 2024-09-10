from django.urls import path
from . import views  # Importa tus vistas desde el mismo módulo
from apps.publico import views as publicoViews

urlpatterns = [
    #DEF
    path('login_user/', views.login_user, name='login_user'),
    #VIEW
    path('login', publicoViews.LoginView.as_view(), name='login'),    

]
