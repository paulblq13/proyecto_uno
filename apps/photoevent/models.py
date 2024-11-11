from django.db import models
from django.utils import timezone
#===CLOUDNARY===
from cloudinary.models import CloudinaryField
#===CLOUDNARY===
   
class EventoTipo(models.Model):
    nombre = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre}"    

class Evento(models.Model):
    nombre_evento = models.CharField(max_length=50, null=True, blank=True)
    fecha_evento = models.DateField (null=True, blank=True)
    cod_eventotipo = models.ForeignKey(EventoTipo, on_delete=models.CASCADE)
    foto_transicion = models.IntegerField(default=10)
    efecto_transicion= models.IntegerField(default=2)
    codigo_evento = models.CharField(max_length=6, unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre_evento}"
    
class Fotos(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado')
    ]
    mensaje = models.CharField(max_length=100)
    #imagen = models.ImageField(upload_to='fotos/')
    imagen = CloudinaryField('imagen', folder='fotos/') 
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente')
    visto = models.BooleanField(default=False)
    fecha_subida = models.DateTimeField(auto_now_add=True)
    fecha_aprobado = models.DateTimeField(null=True, blank=True)
    id_evento = models.ForeignKey(Evento, on_delete=models.CASCADE, null=True, blank=True)

    
    def __str__(self):
        return f"{self.mensaje} - {self.estado}"    
      

