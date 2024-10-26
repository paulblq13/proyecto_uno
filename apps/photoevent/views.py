from django.shortcuts import render, redirect
from .forms import FotoForm
from .models import Fotos

from django.http import JsonResponse
from django.conf import settings

from django.views.generic import ListView


def subir_foto(request):
    if request.method == 'POST':
        form = FotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('subir_foto')
    else:
        form = FotoForm()
    return render(request, 'photoevent/subirfoto.html', {'form': form})


def moderar_fotos(request):
    fotos_pendientes = Fotos.objects.filter(estado='pendiente')
    if request.method == 'POST':
        foto_id = request.POST.get('foto_id')
        accion = request.POST.get('accion')
        foto = Fotos.objects.get(id=foto_id)
        
        if accion == 'aprobar':
            foto.estado = 'aprobado'
        elif accion == 'rechazar':
            foto.estado = 'rechazado'
        
        foto.save()
        return redirect('moderar_fotos')
    
    return render(request, 'photoevent/moderador.html', {'fotos_pendientes': fotos_pendientes})

def lista_fotos_aprobadas(request):
    # Obtener fotos aprobadas, ordenadas por fecha descendente
    fotos_aprobadas = Fotos.objects.filter(estado='aprobado').order_by('-fecha_subida')
    lista_fotos = []
    for foto in fotos_aprobadas:
    # Preparar datos para enviar como JSON
        print(str(settings.MEDIA_URL) + str(foto.imagen))
        fotos_data = {
            'id': foto.id,
            'mensaje': foto.mensaje,
            'imagen': f"{settings.MEDIA_URL}{foto.imagen}"  # Concatenar MEDIA_URL
        }
        lista_fotos.append(fotos_data)
    
    return JsonResponse(lista_fotos, safe=False)


class UltimaFotoView(ListView):
    model = Fotos
    template_name = 'photoevent/galeria_aprobada.html'  # Nombre del template
    context_object_name = 'foto'

    def get_queryset(self):
        return Fotos.objects.filter(estado='aprobado').order_by('-fecha_subida').first()