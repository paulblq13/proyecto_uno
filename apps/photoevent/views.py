from django.shortcuts import render, redirect, get_object_or_404

#==JAVA
from django.http import JsonResponse
from django.conf import settings
#==VIEWS
from django.views.generic import ListView, CreateView, UpdateView, DetailView
#==FORMS
from .forms import EventoForm, FotoForm
#==MODELOS
from .models import Evento, Fotos
#==PILLOW
from PIL import Image, ExifTags
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
#==TIEMPO
from django.utils import timezone
from datetime import datetime
#==OTROS
from django.views.decorators.csrf import csrf_exempt
#===URLS
from django.urls import reverse_lazy
#===CLOUDINARY
#===CLOUDINARY===
import cloudinary
import cloudinary.uploader
#===MENSAJES DE ERROR===
from django.contrib import messages 
#===MENSAJES DE ERROR===

# Configuration       
cloudinary.config( 
    cloud_name = "hchhzysmh", 
    api_key = "296496241944854", 
    api_secret = "83PgLbyixbw5scrBPIzKBFG7N0Q", # Click 'View API Keys' above to copy your API secret
    secure=True
)

#===SUBIR FOTO V3 CLOUDINARY
def subir_fotoV3(request, cod_evento):
    evento = Evento.objects.get(codigo_evento=cod_evento)
    if request.method == 'POST':
        form = FotoForm(request.POST, request.FILES)
        if form.is_valid():
            foto = form.save(commit=False)
            # Crear un nombre único con el código del evento y el timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            nombre_personalizado = f"{evento.codigo_evento}_{timestamp}"
            # Asigna el public_id antes de guardar
            foto.imagen.public_id = f"fotos/{nombre_personalizado}"  # carpeta/fotos/nombre_personalizado
            # Asigna el evento a la foto y guarda
            foto.id_evento = evento
            foto.save()
            messages.success(request, "La foto se ha subido con éxito, será revisada y se mostrará en la pantalla en unos segundos.")
            return redirect('subir_foto', cod_evento=evento.codigo_evento)
    else:
        form = FotoForm()
    return render(request, 'photoevent/subirfoto.html', {'form': form})

#===MODERAR FOTOS===  
def moderar_fotos(request, cod_evento):
    evento = get_object_or_404(
        Evento.objects.prefetch_related(
            'fotos_set'  # Reemplaza 'fotos_set' con el nombre del related_name si tienes uno
        ),
        codigo_evento=cod_evento
    )

    # Filtra solo las fotos pendientes usando una lista de Python
    fotos_pendientes = [foto for foto in evento.fotos_set.all() if foto.estado == 'pendiente']
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
        return redirect('moderar_fotos', cod_evento=evento.codigo_evento)
    
    return render(request, 'photoevent/moderador.html', {'fotos_pendientes': fotos_pendientes})


#===LIVE GALERIA DE EVENTOS===
class LiveGaleriaView(ListView):
    model = Fotos
    template_name = 'photoevent/galeria_aprobada.html'
    context_object_name = 'foto'
    
    def get_queryset(self):
        #===OBJETO EVENTO===
        cod_evento = self.kwargs.get('cod_evento')
        evento = Evento.objects.get(codigo_evento=cod_evento)
        print(evento)
        #===FIN OBJETO EVENTO===        
        # Obtenemos todas las fotos aprobadas en orden ascendente
        return Fotos.objects.filter(estado='aprobado', id_evento=evento.id ).order_by('fecha_aprobado')

    def get_context_data(self, **kwargs):
        #self.request.session['bandera'] = None
        context = super().get_context_data(**kwargs)
        #===OBJETO EVENTO===
        cod_evento = self.kwargs.get('cod_evento')
        evento = get_object_or_404(Evento, codigo_evento=cod_evento)
        print(evento.foto_transicion)
        efecto_transicion = evento.efecto_transicion * 1000
        context['efecto_transicion'] = efecto_transicion
        foto_transicion = evento.foto_transicion * 1000
        context['foto_transicion'] = foto_transicion
        context['imagen_predeterminada'] = evento.foto_predeterminada
        #===FIN OBJETO EVENTO===
        context['codigo_evento'] = evento.codigo_evento
        context['fondo_live'] = evento.fondo_live
        fotos_aprobadas = self.get_queryset()
        foto_index = self.kwargs.get('index')  # Obtener el índice desde la URL
        fotos_aprobadas_list = list(fotos_aprobadas)
        print("CANTIDAD DE FOTOS APROBADAS: " + str(len(fotos_aprobadas_list)))
        print("VALOR DEL INDEX EN URL: " + str(foto_index))
        print("LISTA DE FOTOS APROBADAS: " + str(fotos_aprobadas_list))
        fotos_cantidad = len(fotos_aprobadas_list)
        print("FOTOS_CANTIDAD: " + str(fotos_cantidad))
        if 'siguiente' not in self.request.session:
             self.request.session['siguiente'] = 0
        if fotos_cantidad == 0:
            self.request.session['bandera'] = 0
            bandera = self.request.session['bandera'] 
            print("INICIALIZAR BANDERA: " + str(bandera))
        else:
            if 'bandera' not in self.request.session:
                ultimo_index = fotos_cantidad - 1
                print ("ULTIMO INDEX:" + str(ultimo_index))
                self.request.session['bandera'] = ultimo_index if fotos_aprobadas_list else 0
                bandera = self.request.session['bandera']
                print("RETOMANDO BANDERA EN LA SESION: ", self.request.session['bandera'])
            else:
                # Obtener el valor actual de la bandera
                bandera = self.request.session['bandera']
                print("SI YA ESTÁ LA BANDERA EN LA SESION: ", bandera)
        #==================================SI LA URL ESTÁ VACIA
        if foto_index is None: 
            # Si no hay id, muestra la imagen predeterminada
           
            context['mostrar_predeterminada'] = True
            context['foto_actual'] = None
            # Buscar si existe una nueva foto aprobada con ID mayor que la bandera
            nueva_foto = fotos_cantidad > bandera
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
                    play=self.request.session['siguiente'] 
                    print("siguiente index_play: " + str(play))
                    context['siguiente'] = play
                else:
                    context['siguiente_index'] = None
                    siguiente_index=self.request.session['siguiente'] 
                    print("siguiente index: " + str(siguiente_index))
            else:
                print("NO EXISTE NUEVA FOTO")                
                context['siguiente_index'] = None
                play=self.request.session['siguiente'] 
                print("siguiente index: " + str(play))
                if play == 0:
                    print("play == 0")
                    context['siguiente'] = play
                else:  
                    print("play - 1") 
                    context['siguiente'] = play
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
                self.request.session['siguiente'] = foto_index + 1
                siguiente_index=foto_index + 1
                print("siguiente index: " + str(siguiente_index))
                context['siguiente_index'] = foto_index + 1
            else:
                context['siguiente_index'] = None
                self.request.session['siguiente'] = foto_index
                siguiente_index= foto_index
                print("siguiente index: " + str(foto_index))
        return context
         

#===GALERIA DE FOTOS===
class GaleriaFotosView(ListView):
    model = Fotos
    template_name = 'photoevent/galeria_fotos.html'
    context_object_name = 'object'
    
    def get_queryset(self):
        # Obtenemos todas las fotos aprobadas en orden ascendente
        #===OBJETO EVENTO===
        cod_evento = self.kwargs.get('cod_evento')
        evento = Evento.objects.get(codigo_evento=cod_evento)
        print(evento)
        #===FIN OBJETO EVENTO===        
        return Fotos.objects.filter(estado='aprobado', id_evento=evento.id).order_by('-fecha_subida')    

#===LISTADO DE EVENTOS===
class PhotoEventListaView(ListView):
    template_name = 'photoevent/lista-evento.html'
    model= Evento
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk=self.kwargs.get('pk', 0)
        object_list = Evento.objects.all()
        print(object_list)
        context['lista'] = "LISTA"
        context['titulo'] = "LISTADO DE EVENTOS"
        context['titulosmall'] = "Lista de eventos"
        context['url_nuevo'] = "/photoevent/agregar"
        context['url_modificar'] = "modificar-evento"
        context['url_detalle'] = "detalle-evento"
        context['url_eliminar'] = "eliminar-evento"
        return context       


#===EVENTONUEVO===
class addEventoView(CreateView):
    model = Evento
    template_name = 'photoevent/addedit-evento.html'
    form_class = EventoForm
    success_url = reverse_lazy('photoevent-lista')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        context['titulo']="NUEVO"
        context['lista']="LISTA"
        context['tituloh2'] = "Agregue o modifique datos de algun vendedor"
        context['titulosmall']="Ingrese los datos requeridos y luego presione GUARDAR"
        context['urllegajo'] = "verLegajoPersona"
        context['id'] = pk
        context['bandera_add_update'] = "add"
        return context
    def form_valid(self, form):
        # Procesa el formulario correctamente, incluyendo el archivo de imagen
        if 'foto_predeterminada' in self.request.FILES:
            form.instance.foto_predeterminada = self.request.FILES['foto_predeterminada']
        return super().form_valid(form)
 
    #POST
        #PERSONA EXISTE?
            #SI
            #PERSONA YA ES VENDEDOR?
                #SI: ACTUALIZAR DATOS
                #NO: ACTUALIZAR Y DAR DE ALTA EN VENDEDOR
            #NO
                #DAR DE ALTA PERSONA
                #DAR DE ALTA VENDEDOR

#===EVENTOUPDATE===
class updateEventoView(UpdateView):
    model = Evento
    template_name = 'photoevent/addedit-evento.html'
    form_class = EventoForm
    success_url = reverse_lazy('photoevent-lista')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        context['titulo'] = 'MODIFICAR'
        context['tituloh2'] = 'Modificar evento'
        context['titulosmall'] = 'Complete los campos requeridos y luego presiones el botón GUARDAR'
        return context
    
    def form_valid(self, form):
        # Procesa el formulario correctamente, incluyendo el archivo de imagen
        if 'foto_predeterminada' in self.request.FILES:
            form.instance.foto_predeterminada = self.request.FILES['foto_predeterminada']
        return super().form_valid(form)             

#===EVENTOSDETALLES===
class detallesEventoView(DetailView):

    model=Evento
    template_name='photoevent/detalle-evento.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk=self.kwargs.get('pk', 0)
        solicitud = self.model.objects.get(id=pk)
        print("SOLICITUD: "+str(solicitud.foto_transicion))
        unidad=self.model.objects.get(id=pk)
        #print("UNIDAD: "+str(unidad.unidades_detencion.id))

        context['anio_actual'] = timezone.now().year
        context['titulo']="INFORMACIÓN"
        context['tituloh2'] = "Información del evento"
        context['titulosmall']="Aquí se muestra toda la información correspondiente"
        context['id_solicitud'] = solicitud.id
        context['foto_transicion'] = solicitud.foto_transicion
        context['efecto_transicion'] = solicitud.efecto_transicion
        context['nombre_evento'] = solicitud.nombre_evento
        context['codigo_evento'] = solicitud.codigo_evento
        return context
    
#===INGRESARCODIGO===
def ingresar_codigo(request):
    if request.method == 'POST':
        cod_evento = request.POST.get('cod_evento')   
        # Verificar que el código sea de 6 dígitos
        if cod_evento and cod_evento.isdigit() and len(cod_evento) == 6:
            # Aquí deberías verificar si el código existe, por ejemplo:
            evento_existe = Evento.objects.filter(codigo_evento=cod_evento).exists()
            #evento_existe = True  # Cambia esto según tu lógica para verificar existencia
            if evento_existe:
                print("EXISTE")
                return redirect('subir_foto', cod_evento=int(cod_evento))
            else:
                print("NO EXISTE")
                messages.error(request, "El código de evento no existe.")
        else:
            messages.error(request, "Por favor, ingrese un código válido de 6 dígitos.")
    # Renderiza la plantilla con el formulario y cualquier mensaje
    return render(request, 'publico/publico.html')