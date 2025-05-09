from django.contrib import admin

from apps.todoventas.models import Categorias, Depositos, Personas, Productos, Proveedores

#Categorias
class categoriasAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre',)
    search_fields = ('id', 'nombre',)
admin.site.register(Categorias, categoriasAdmin)

#Depositos
class depositosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre',)
    search_fields = ('id', 'nombre',)
admin.site.register(Depositos, depositosAdmin)

#Personas
class personasAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre',)
    search_fields = ('id', 'nombre',)
admin.site.register(Personas, personasAdmin)

#Proveedores
class proveedoresAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre',)
    search_fields = ('id', 'nombre',)
admin.site.register(Proveedores, proveedoresAdmin)

#Productos
class productosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre',)
    search_fields = ('id', 'nombre',)
admin.site.register(Productos, productosAdmin)



