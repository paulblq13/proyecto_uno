from django.contrib import admin
# Register your models here.
from apps.noticias.models import Noticia

class noticiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo')
    search_fields = ('titulo', )

admin.site.register(Noticia, noticiaAdmin)
