from django.shortcuts import render
from django.views.generic import ListView
from apps.noticias.models import Noticia

    #-------------------------------LISTA DESTINOS
class listNoticiasView(ListView):
    template_name = 'noticias/list_noticias.html'
    model= Noticia

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk=self.kwargs.get('pk', 0)
        object_list = Noticia.objects.all()
        print(object_list)
        context['lista'] = "DESTINOS"
        context['titulo'] = "LISTADO DE DESTINOS"
        context['titulosmall'] = "Lista de destinos"
        context['url_nuevo'] = "nuevo-destino"
        context['url_modificar'] = "modificar-destino"
        context['url_detalle'] = "detalle-destino"
        context['url_eliminar'] = "eliminar-destino"
        return context
