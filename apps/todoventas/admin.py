from django.contrib import admin

from apps.todoventas.models import Categorias, Productos

#Categorias
class categoriasAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre',)
    search_fields = ('id', 'nombre',)

admin.site.register(Categorias, categoriasAdmin)
#Productos
class productosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre',)
    search_fields = ('id', 'nombre',)

admin.site.register(Productos, productosAdmin)