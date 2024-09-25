from django.urls import path
from . import views  # Importa tus vistas desde el mismo módulo
from apps.usuario import views as usuarioViews

urlpatterns = [
    #DEF
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logoutDef, name='logout_user'),
    #VIEW
    path('login/', usuarioViews.LoginView.as_view(), name='login'),
]
