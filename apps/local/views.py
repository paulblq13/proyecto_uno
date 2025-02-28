from django.http import JsonResponse
from django.shortcuts import render
#==VIEWS
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, TemplateView

from apps.local.forms import ArticuloForm, FacturaEgresoDetalleForm, FacturaEgresoForm
from apps.local.models import Articulo, FacturaEgreso, FacturaEgresoDetalle
 


 #===HOME LOCAL===
class homeLocalView(TemplateView):
    template_name = 'local/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk=self.kwargs.get('pk', 0)
        context['lista'] = "LISTA"
        context['titulo'] = "PANEL DE CONTROL"
        context['titulosmall'] = "Panel de control"
        context['url_nuevo'] = "/photoevent/agregar"
        context['url_modificar'] = "modificar-evento"
        context['url_detalle'] = "detalle-evento"
        context['url_eliminar'] = "eliminar-evento"
        return context       



 #===LISTADO DE PRODUCTOS===
class productosView(TemplateView):
    template_name = 'local/lista-articulos.html'
    model = Articulo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk=self.kwargs.get('pk', 0)
        context['object_list'] = Articulo.objects.all()
        context['lista'] = "LISTA"
        context['titulo'] = "GESTIÓN DE PRODUCTOS"
        context['titulosmall'] = "Gestión de productos"
        context['url_nuevo'] = "/local/agregar-articulo/"
        context['url_modificar'] = "modificar-evento"
        context['url_detalle'] = "detalle-evento"
        context['url_eliminar'] = "eliminar-evento"
        return context    
    
#===AGREGAR ARTICULO ===
class addArticuloView(CreateView):
    model = Articulo
    template_name = 'local/addedit-articulo.html'
    form_class = ArticuloForm
    success_url = reverse_lazy('lista-productos')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        context['titulo']="NUEVO"
        context['descripcion_pantalla'] = "Complete los datos requeridos para agregar un nuevo artículo"        
        context['lista']="LISTA"
        context['tituloh2'] = "Agregue o modifique datos del artículo"
        context['titulosmall']="Ingrese los datos requeridos y luego presione GUARDAR"
        context['urllegajo'] = "verLegajoPersona"
        context['url_nuevo'] = "agregar-articulo"
        context['id'] = pk
        context['bandera_add_update'] = "add"
        return context
 
#===MODIFICAR ARTICULO===
class updateArticuloView(UpdateView):
    model = Articulo
    template_name = 'local/addedit-articulo.html'
    form_class = ArticuloForm
    success_url = reverse_lazy('lista-productos')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        context['titulo'] = 'MODIFICAR'
        context['tituloh2'] = 'Modificar evento'
        context['descripcion_pantalla'] = "Modificá los datos requeridos y luego presiona el botón GUARDAR"             
        return context
    
 #===LISTADO DE VENTAS===
class listaVentasView(ListView):
    template_name = 'local/lista-ventas.html'
    model = FacturaEgreso

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk=self.kwargs.get('pk', 0)

        context['nivel_anterior'] = "KIOSCO"
        context['lista'] = "LISTA"
        context['titulo'] = "GESTIÓN DE VENTAS"
        context['descripcion_pantalla'] = "Muestra un listado de las ventas realizadas"
        context['titulosmall'] = "Gestión de ventas"
        context['boton_nuevo'] = "NUEVA VENTA"
        context['url_nuevo'] = "/local/agregar-venta/"
        context['url_modificar'] = "modificar-evento"
        context['url_detalle'] = "detalle-evento"
        context['url_eliminar'] = "eliminar-evento"

        return context      
    
#===NUEVA VENTA ===
class addVentaView(CreateView):
    model = FacturaEgreso
    second_model = FacturaEgresoDetalle
    template_name = 'local/addedit-nueva_venta.html'
    form_class = FacturaEgresoForm
    second_form_class = FacturaEgresoDetalleForm
    success_url = reverse_lazy('lista-productos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        context['form'] = self.form_class(self.request.GET)
        context['form2'] = self.second_form_class(self.request.GET)

        articulos=Articulo.objects.all()
        print(articulos)
        lista_articulos = Articulo.objects.all()
        print(lista_articulos)

        context['lista_articulos'] = lista_articulos
        context['nivel_anterior'] = "KIOSCO"            
        context['titulo']="NUEVO"
        context['descripcion_pantalla'] = "Complete los datos requeridos para agregar un nuevo artículo"        
        context['lista']="LISTA"
        context['tituloh2'] = "Agregue o modifique datos del artículo"
        context['titulosmall']="Ingrese los datos requeridos y luego presione GUARDAR"
        context['urllegajo'] = "verLegajoPersona"
        context['url_nuevo'] = "agregar-articulo"
        context['id'] = pk
        context['bandera_add_update'] = "add"
        return context    
    

def search_articulos(request):
    print("hola")
    query = request.GET.get('q', '')
    articulos = Articulo.objects.filter(nombre__icontains=query)[:10]  # Filtra los artículos por nombre
    results = [{'id': articulo.id, 'text': articulo.nombre} for articulo in articulos]  # Formato necesario para select2
    return JsonResponse({'results': results})    