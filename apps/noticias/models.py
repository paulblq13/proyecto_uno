from django.db import models
from django.utils import timezone

class Noticia(models.Model):
    ESTADO_CHOICES = [
        ('borrador', 'Borrador'),
        ('pendiente', 'Pendiente de revisión'),
        ('publicado', 'Publicado'),
    ]
    
    VISIBILIDAD_CHOICES = [
        ('publico', 'Público'),
        ('contrasena', 'Con contraseña'),
        ('privado', 'Privado'),
    ]
    
    titulo = models.CharField(max_length=200)
    cuerpo = models.TextField()
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='borrador')
    visibilidad = models.CharField(max_length=10, choices=VISIBILIDAD_CHOICES, default='publico')
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    fecha_programada_publicacion = models.DateTimeField(null=True, blank=True)
    seccion = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo