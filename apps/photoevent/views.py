from django.shortcuts import render, redirect, get_object_or_404

#==JAVA
from django.http import JsonResponse
from django.conf import settings
#==VIEWS
from django.views.generic import ListView
#==FORMS
from .forms import FotoForm
#==MODELOS
from .models import Fotos
#==PILLOW
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
#==TIEMPO
from django.utils import timezone
from datetime import datetime
#==OTROS
from django.views.decorators.csrf import csrf_exempt

def subir_foto(request):
    if request.method == 'POST':
        form = FotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('subir_foto')
    else:
        form = FotoForm()
    return render(request, 'photoevent/subirfoto.html', {'form': form})

def subir_fotoV2(request):
    if request.method == 'POST':
        form = FotoForm(request.POST, request.FILES)
        if form.is_valid():
            foto = form.save(commit=False)
            imagen = Image.open(foto.imagen)

            # Dimensiones para pantalla Full HD
            ancho_deseado = 1920
            alto_deseado = 1080

            # Obtener dimensiones originales
            ancho_original, alto_original = imagen.size

            # Calcular la relación de aspecto
            relacion_aspecto = ancho_original / alto_original        

            # Calcular el nuevo alto y ancho
            nuevo_alto = alto_deseado
            nuevo_ancho = int(nuevo_alto * relacion_aspecto)                

            # Si el nuevo ancho supera el límite deseado, ajusta el ancho
            if nuevo_ancho > ancho_deseado:
                nuevo_ancho = ancho_deseado
                nuevo_alto = int(nuevo_ancho / relacion_aspecto)

            # Redimensionar la imagen
            nueva_imagen = imagen.resize((nuevo_ancho, nuevo_alto), Image.LANCZOS)

            # Convertir a RGB si es necesario
            if nueva_imagen.mode == 'RGBA':
                nueva_imagen = nueva_imagen.convert('RGB')
            elif nueva_imagen.mode == 'P':
                nueva_imagen = nueva_imagen.convert('RGB')

            # Generar un nombre único con la fecha y hora
            timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            foto.imagen.name = f"photoevent_{timestamp}.jpg"

            # Guardar la imagen redimensionada
            buffer = BytesIO()
            nueva_imagen.save(buffer, format='JPEG')
            buffer.seek(0)

            # Reemplazar la imagen original por la nueva
            foto.imagen = InMemoryUploadedFile(
                buffer, 'ImageField', foto.imagen.name, 'image/jpeg', buffer.getbuffer().nbytes, None
            )
            foto.save()

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
            foto.fecha_aprobado = timezone.now()
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
        return Fotos.objects.filter(estado='aprobado').order_by('fecha_aprobado')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fotos_aprobadas = self.get_queryset()
        foto_index = self.kwargs.get('index')  # Obtener el índice desde la URL
        # Convierte queryset a una lista de fotos aprobadas
        fotos_aprobadas_list = list(fotos_aprobadas)        
        print("1)fotos_aprobadas_list " + str(len(fotos_aprobadas_list)))
        # Inicializar la BANDERA en la sesión
        fotos_cantidad = Fotos.objects.filter(estado='aprobado').count()
        if fotos_cantidad == 0:
            self.request.session['bandera'] = 0
            bandera = self.request.session['bandera'] 
            print(bandera)
        else:
            if 'bandera' not in self.request.session:
                self.request.session['bandera'] = fotos_aprobadas_list[0] if fotos_aprobadas_list else 0    
                print("Inicializando bandera en la sesión:", self.request.session['bandera'])
            else:
                # Obtener el valor actual de la bandera
                bandera = self.request.session['bandera']
                print("Valor actual de bandera en la sesión:", bandera)                     
                                
          
            
#==================================SI LA URL ESTÁ VACIA
        if foto_index is None: 
            # Si no hay id, muestra la imagen predeterminada
           
            context['mostrar_predeterminada'] = True
            context['foto_actual'] = None
            # Buscar si existe una nueva foto aprobada con ID mayor que la bandera
            nueva_foto = len(fotos_aprobadas_list) > bandera
            print("NUEVA_FOTO?" +str(nueva_foto))
            if nueva_foto:
                siguiente_index = bandera
                if siguiente_index < len(fotos_aprobadas_list):
                    context['mostrar_predeterminada'] = True
                    context['mostrar_predeterminada_salir'] = True
                    foto_index = int(siguiente_index)
                    foto_actual = fotos_aprobadas_list[foto_index]   
                    print("foto_actual_ID: "+str(foto_actual.id))                 
                    context['foto_actual'] = foto_actual
                    context['ultima_foto'] = False       
                    context['siguiente_index'] = foto_index
                    print("siguiente index:", siguiente_index)    

                else:
                    context['siguiente_index'] = None
            else:
                print("NO EXISTE NUEVA FOTO")                
                context['siguiente_index'] = None
#==================================SI LA URL TIENE UN ID              
        else:
            # Cargar la foto actual y verificar si es la última
            #foto_actual = get_object_or_404(Fotos, id=foto_id, estado='aprobado')
            context['mostrar_predeterminada'] = False
            context['mostrar_predeterminada_salir'] = False            
            foto_index = int(foto_index)
            print("foto_index: " + str(foto_index))
            foto_actual = fotos_aprobadas_list[foto_index]
            print("foto_actual: " + str(foto_actual))
            context['foto_actual'] = foto_actual
            ultima_foto = (foto_index == len(fotos_aprobadas_list) - 1)
            print("3 - ultima_foto: " +str(ultima_foto))
            context['ultima_foto'] = ultima_foto
            if ultima_foto:
                # Guardar el índice actual en la sesión para futuros usos
                self.request.session['bandera'] = foto_index + 1
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