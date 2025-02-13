from django.shortcuts import render
#==VIEWS
from django.views.generic import ListView, CreateView, UpdateView, DetailView, TemplateView
 


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
    template_name = 'local/lista-productos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk=self.kwargs.get('pk', 0)
        context['lista'] = "LISTA"
        context['titulo'] = "GESTIÓN DE PRODUCTOS"
        context['titulosmall'] = "Gestión de productos"
        context['url_nuevo'] = "/photoevent/agregar"
        context['url_modificar'] = "modificar-evento"
        context['url_detalle'] = "detalle-evento"
        context['url_eliminar'] = "eliminar-evento"
        return context    