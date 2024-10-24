from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
#==FOTOS TIEMPO REAL==
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
#==FIN FOTOS TIEMPO REAL==

#-----------------------VIEWS-------------------------
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'publico/publico.html'

class Invitacion01View(TemplateView):
    template_name = 'publico/invitacion_01.html'    

class Invitacion02View(TemplateView):
    template_name = 'publico/invitacion_02.html'       

class Invitacion03View(TemplateView):
    template_name = 'publico/invitacion_03.html'      

class EscritorioView(TemplateView):
    template_name = 'publico/escritorio.html'

def upload_photo(request):
    if request.method == 'POST' and request.FILES['photo']:
        photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(photo.name, photo)
        return render(request, 'upload_success.html', {'filename': filename})
    return render(request, 'upload_photo.html')

def gallery(request):
    photos = FileSystemStorage().listdir('')[1]  # Listar todas las fotos
    return render(request, 'gallery.html', {'photos': photos})