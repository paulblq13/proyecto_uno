from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
#==FOTOS==
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
#==FIN FOTOS==
#TIEMPO REAL=========
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.conf import settings
#======FIN TIEMPO REAL

#-----------------------VIEWS-------------------------
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'publico/index.html'

class Invitacion01View(TemplateView):
    template_name = 'tuinvitacionvirtual/invitacion_01.html'    

class Invitacion02View(TemplateView):
    template_name = 'tuinvitacionvirtual/invitacion_02.html'       

class Invitacion03View(TemplateView):
    template_name = 'tuinvitacionvirtual/invitacion_03.html'      

class EscritorioView(TemplateView):
    template_name = 'publico/escritorio.html'

def upload_photo(request):
    if request.method == 'POST' and request.FILES['photo']:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'gallery_group',  # Nombre del grupo de la galería
            {
                'type': 'new_image',
                'message': 'Nueva imagen subida'
            }
        )        
        photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(photo.name, photo)
        return redirect(f'{settings.MEDIA_URL}')
    return render(request, 'publico/upload_fotos.html')

def photo_gallery(request):
    photos = FileSystemStorage().listdir('')[1]  # Listar todas las fotos
    return render(request, 'publico/upload_galeria.html', {'photos': photos})