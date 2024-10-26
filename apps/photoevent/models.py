from django.db import models
from django.utils import timezone

class Fotos(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado')
    ]
    mensaje = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='fotos/')
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente')
    fecha_subida = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.mensaje} - {self.estado}"