from django.shortcuts import render, redirect
from django.db import transaction
#===========VIEWS
from django.views.generic import ListView, CreateView
#===========FORMULARIOS
from apps.noticias.forms import NoticiasForm
#=========MODELOS
from apps.noticias.models import Noticia
#==========USUARIO
from django.contrib.auth.models import Group, User

    #-------------------------------LISTA DESTINOS
class listNoticiasView(ListView):
    template_name = 'noticias/list_noticias.html'
    model= Noticia

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk=self.kwargs.get('pk', 0)
        object_list = Noticia.objects.all()
        print(object_list)
        context['lista'] = "NOTICIAS"
        context['titulo'] = "LISTADO DE NOTICIAS"
        context['titulosmall'] = "Lista de noticias"
        context['url_nuevo'] = "/nueva-noticia"
        context['url_modificar'] = "modificar-noticia"
        context['url_detalle'] = "detalle-noticia"
        context['url_eliminar'] = "eliminar-noticia"
        return context


#---------------------------NOTICIA NUEVO y UPDATE---------------
class addNoticiaView(CreateView):
    model = Noticia
    template_name = 'noticias/addedit-noticia.html'
    form_class = NoticiasForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        context['titulo']="NUEVO"
        context['tituloh2'] = "Agregue o modifique datos de algun vendedor"
        context['titulosmall']="Ingrese los datos requeridos y luego presione GUARDAR"
        context['urllegajo'] = "verLegajoPersona"
        context['id'] = pk
        context['bandera_add_update'] = "add"
        return context
    #POST
        #PERSONA EXISTE?
            #SI
            #PERSONA YA ES VENDEDOR?
                #SI: ACTUALIZAR DATOS
                #NO: ACTUALIZAR Y DAR DE ALTA EN VENDEDOR
            #NO
                #DAR DE ALTA PERSONA
                #DAR DE ALTA VENDEDOR
