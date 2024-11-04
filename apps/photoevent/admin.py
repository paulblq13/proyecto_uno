from django.contrib import admin
# Register your models here.
from apps.photoevent.models import Fotos, Evento, EventoTipo

class fotosAdmin(admin.ModelAdmin):
    list_display = ('id', 'mensaje', 'fecha_aprobado')
    search_fields = ('mensaje', )

admin.site.register(Fotos, fotosAdmin)


class eventosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_evento', 'fecha_evento')
    search_fields = ('nombre_evento', )

admin.site.register(Evento, eventosAdmin)

class eventotipoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre', )

admin.site.register(EventoTipo, eventotipoAdmin)
