from django.contrib import admin
# Register your models here.
from apps.photoevent.models import Fotos

class fotosAdmin(admin.ModelAdmin):
    list_display = ('id', 'mensaje', 'fecha_aprobado')
    search_fields = ('mensaje', )

admin.site.register(Fotos, fotosAdmin)