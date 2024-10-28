from django.shortcuts import render, redirect, get_object_or_404
from .forms import FotoForm
from .models import Fotos

from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

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
    template_name = 'photoevent/galeria_aprobada.html'
    context_object_name = 'foto'


    def get_queryset(self):
        # Obtenemos todas las fotos aprobadas en orden ascendente
        return Fotos.objects.filter(estado='aprobado').order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fotos_aprobadas = self.get_queryset()
        foto_index = self.kwargs.get('index')  # Obtener el índice desde la URL
        # Convierte queryset a una lista de fotos aprobadas
        fotos_aprobadas_list = list(fotos_aprobadas)        
        print("1 fotos_aprobadas_list " +str(fotos_aprobadas_list))

        # Inicializar la bandera en la sesión
        if 'bandera' not in self.request.session:
            self.request.session['bandera'] = fotos_aprobadas_list[0] if fotos_aprobadas_list else 0    
            print("Inicializando bandera en la sesión:", self.request.session['bandera'])
        else:
            # Obtener el valor actual de la bandera
            bandera_actual = self.request.session['bandera']
            print("Valor actual de bandera en la sesión:", bandera_actual)

   

        if foto_index is None: #SI LA URL ESTÁ VACIA
            # Si no hay id, muestra la imagen predeterminada
            context['mostrar_predeterminada'] = True
            context['foto_actual'] = None
            # Buscar si existe una nueva foto aprobada con ID mayor que la bandera
            nueva_foto = len(fotos_aprobadas_list) > bandera_actual
            print("NUEVA_FOTO?" +str(nueva_foto))
            if nueva_foto:
                print("siguiente index: " )
         
              
        else: #SI LA URL TIENE UN ID
            # Cargar la foto actual y verificar si es la última
            #foto_actual = get_object_or_404(Fotos, id=foto_id, estado='aprobado')
            foto_index = int(foto_index)
            foto_actual = fotos_aprobadas_list[foto_index]
            context['foto_actual'] = foto_actual
            print(" si foto actual es igual a fotos aprobadas id - 1: " +str(foto_actual.id) + "/" + str(fotos_aprobadas_list[-1]))
            ultima_foto = (foto_index == len(fotos_aprobadas_list) - 1)

            print("3 - ultima_foto: " +str(ultima_foto))
            context['ultima_foto'] = ultima_foto


            if ultima_foto:
                # Guardar el índice actual en la sesión para futuros usos
                self.request.session['bandera'] = foto_index
                print("Actualizando bandera al último índice:", self.request.session['bandera'])


            # Determinar el índice siguiente y agregarlo al contexto
            if not ultima_foto:
                context['siguiente_index'] = foto_index + 1
            else:
                context['siguiente_index'] = None
                
        return context
        
@csrf_exempt
def actualizar_ultima_foto(request):
    if request.method == 'POST':
        # Cambiar el valor de ultima_foto en la sesión o en la base de datos
        request.session['ultima_foto'] = True
        return JsonResponse({'status': 'success'})
    
    return JsonResponse({'status': 'failed'})   