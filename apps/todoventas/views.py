from django.http import JsonResponse
from django.shortcuts import render
#==VIEWS
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, TemplateView

from apps.local.forms import ArticuloForm, FacturaEgresoDetalleForm, FacturaEgresoForm
from apps.local.models import Articulo, FacturaEgreso, FacturaEgresoDetalle
 


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
