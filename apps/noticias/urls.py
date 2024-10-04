from django.urls import path
from . import views  # Importa tus vistas desde el mismo módulo
from django.contrib.auth.decorators import login_required
from apps.noticias import views as noticiasViews

urlpatterns = [
    #DEF
    #path('login_user/', views.login_user, name='login_user'),

    #VIEW
    #path('login/', usuarioViews.LoginView.as_view(), name='login'),
    path('lista-noticias/', login_required(noticiasViews.listNoticiasView.as_view()), name="lista-noticias"),  
#------------ADD VIEW
    path('nueva-noticia/', login_required(noticiasViews.addNoticiaView.as_view()), name="nueva-noticia"),         
]
