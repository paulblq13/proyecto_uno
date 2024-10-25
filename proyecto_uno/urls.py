"""
URL configuration for proyecto_uno project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin

#=========================PARA IMAGENES
from django.conf import settings
from django.conf.urls.static import static
#FIN PARA IMAGENES======================
from django.urls import path, include
from apps.publico import views as publicoViews

urlpatterns = [
    path('admin/', admin.site.urls),
    #--------VIEW
    path('', publicoViews.IndexView.as_view(), name=''),
    path('index/', publicoViews.IndexView.as_view(), name='index'),
    path('publico/', publicoViews.IndexView.as_view(), name='publico'),
    #INCLUDES URL   
    path('', include('apps.publico.urls')),
    path('', include('apps.usuario.urls')),
    path('', include('apps.noticias.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
