from django.http import JsonResponse
from django.shortcuts import get_object_or_404
#==VIEWS
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, TemplateView

from apps.local.forms import ArticuloForm, FacturaEgresoDetalleForm, FacturaEgresoForm
from apps.local.models import Articulo, FacturaEgreso, FacturaEgresoDetalle
from apps.todoventas.models import Categorias, Productos
 


 #===HOME TODOVENTAS===
class homeTodoVentasView(TemplateView):
    template_name = 'todoventas/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk=self.kwargs.get('pk', 0)
        context['lista'] = "LISTA"
        context['titulo'] = "PANEL DE CONTROL"
        context['titulosmall'] = "Panel de control"
        context['url_nuevo'] = "/todoventas/agregar"
        context['url_modificar'] = "modificar-evento"
        context['url_detalle'] = "detalle-evento"
        context['url_eliminar'] = "eliminar-evento"
        return context       

 #===LISTA PRODUCTOS===
class listaProductosView(ListView):
    template_name = 'todoventas/lista_productos.html'
    model=Productos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk=self.kwargs.get('pk', 0)
        context['lista'] = "LISTA"
        context['titulo'] = "PANEL DE CONTROL"
        context['titulosmall'] = "Panel de control"
        #context['url_nuevo'] = "/todoventas/agregar"
        #context['url_modificar'] = "modificar-evento"
        #context['url_detalle'] = "detalle-evento"
        #context['url_eliminar'] = "eliminar-evento"
        return context       
    
    # ------------------------------------------LISTAS DE CLAVES ----------------------------------------
class listaCategoriasView(ListView):
    template_name = 'todoventas/lista_categorias.html'
    model= Categorias
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #CONTEXTS
        context['nivel_uno'] = "INICIO"
        context['nivel_dos'] = "TODOVENTAS"
        context['nivel_dos_link'] = "todoventas"
        context['nivel_tres'] = ""
        context['nivel_actual'] = "GESTIÓN DE CATEGORÍAS"
        context['titulo_nuevo_modal'] = "Nueva categoría"
        context['urleliminar'] ="/sistemas/eliminar_registro/"
        context['btnNuevo'] = "NUEVA CATEGORÍA" 
        context['nuevo_titulo'] = "Agregar nueva categoría"
        context['modificar_titulo'] = "Modificar datos"           
        context['nuevo_descripcion'] = "Complete los campos requeridos (*) y luego presione el botón GUARDAR"
        context['modificar_descripcion'] = "Modifique los campos necesarios y luego presione el botón GUARDAR"        
        context['titulo'] = "LISTA DE CATEGORÍAS"
        context['tituloh2'] = "Listado de categorías"
        context['titulosmall'] = "El siguiente listado muestra las categorías guardadas, si lo desea puede copiar la tabla, exportarla para trabajar como una hoja de cálculo o simplemente imprimirlo."
        return context    
    
#_------------------------------ALTA DE CLAVE MODAL----------------
def nuevo_registro(request):
    print("GUARDAR ARTICULO")
    if request.method == 'POST':
        nombre = request.POST.get('campo1')
        observacion = request.POST.get('campo2')

        nuevo_registro = Categorias(
            nombre = nombre,
            observacion = observacion,
            )
        nuevo_registro.save()
        response_data = {
            'guardado': 'ok'
        }
        return JsonResponse(response_data, status=201)

    return JsonResponse({'mensaje': 'Método no permitido.'}, status=405)      

#_------------------------------OBTENER REGISTRO MODAL----------------

def obtener_registro(request):
    id = request.POST.get('id')
    try:
        registro = get_object_or_404(Categorias, id=id)
        return JsonResponse({
            'id': registro.id,
            'nombre': registro.nombre,
            'observacion': registro.observacion,
            #'sede_nombre': registro.sede.nombre if registro.sede else "No registra",
        })
    except Categorias.DoesNotExist:
        return JsonResponse({'error': 'Registro no encontrado'}, status=404)
    

#_------------------------------ACTUALIZAR REGISTRO MODAL----------------
def actualizar_registro(request):
    if request.method == 'POST':
        campo_id = request.POST.get('campo_id')
        nombre = request.POST.get('campo1')
        observacion = request.POST.get('campo2')
        try:
            objeto = Categorias.objects.get(id=campo_id)
        except Categorias.DoesNotExist:
            return JsonResponse({'guardado': 'error', 'mensaje': 'Registro no encontrado'}, status=404)        

        objeto.nombre=nombre
        objeto.observacion=observacion
        objeto.save()
        response_data = {
            'guardado': 'ok'
        }
        return JsonResponse(response_data, status=201)

    return JsonResponse({'mensaje': 'Método no permitido.'}, status=405)      

    # ------------------------------------------GESTION VENTAS ----------------------------------------
class gestionVentasView(ListView):
    template_name = 'todoventas/gestion_ventas.html'
    model= Productos
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #CONTEXTS
        context['nivel_uno'] = "INICIO"
        context['nivel_dos'] = "TODOVENTAS"
        context['nivel_dos_link'] = "todoventas"
        context['nivel_tres'] = ""
        context['nivel_actual'] = "GESTIÓN DE VENTAS"
        context['titulo_nuevo_modal'] = "Nueva categoría"
        context['urleliminar'] ="/sistemas/eliminar_registro/"
        context['btnNuevo'] = "NUEVA VENTA" 
        context['nuevo_titulo'] = "Agregar nueva venta"
        context['modificar_titulo'] = "Modificar datos"           
        context['nuevo_descripcion'] = "Complete los campos requeridos (*) y luego presione el botón GUARDAR"
        context['modificar_descripcion'] = "Modifique los campos necesarios y luego presione el botón GUARDAR"        
        context['titulo'] = "LISTA DE CATEGORÍAS"
        context['tituloh2'] = "Listado de categorías"
        context['titulosmall'] = "El siguiente listado muestra las categorías guardadas, si lo desea puede copiar la tabla, exportarla para trabajar como una hoja de cálculo o simplemente imprimirlo."
        return context 