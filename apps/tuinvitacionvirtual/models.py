from django.db import models
from django.utils import timezone
#===CLOUDNARY===
from cloudinary.models import CloudinaryField
#===CLOUDNARY===
from apps.photoevent.models import EventoTipo

  
class Invitacion(models.Model):
    nombre = models.CharField(max_length=40, null=True, blank=True)
    fecha = models.DateField (null=True, blank=True)
    hora = models.TimeField (null=True, blank=True)
    cod_eventotipo = models.ForeignKey(EventoTipo, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    #logo_png = models.ImageField(upload_to='fotos/')
    logo_png = CloudinaryField('imagen', folder="invitaciones_logos")
    logo_musica_play = CloudinaryField('imagen', folder="invitaciones_musica")
    logo_musica_stop = CloudinaryField('imagen', folder="invitaciones_musica")
    foto01 = CloudinaryField('imagen', folder="invitaciones_fotos")
    foto02 = CloudinaryField('imagen', folder="invitaciones_fotos")
    foto03 = CloudinaryField('imagen', folder="invitaciones_fotos")
    color1 = models.CharField(max_length=7, null=True, blank=True) 
    color2 = models.CharField(max_length=7, null=True, blank=True)
    letra_color1 = models.CharField(max_length=7, null=True, blank=True)
    letra_color2 = models.CharField(max_length=7, null=True, blank=True)
    letra_color3 = models.CharField(max_length=7, null=True, blank=True)
    insta = models.CharField(max_length=15, null=True, blank=True)
    fondo1= CloudinaryField('imagen', folder="invitaciones_fondos")
    fondo2= CloudinaryField('imagen', folder="invitaciones_fondos")
    fondo3= CloudinaryField('imagen', folder="invitaciones_fondos")
    fondo4= CloudinaryField('imagen', folder="invitaciones_fondos")
    fondo_video = models.CharField(max_length=255, null=True, blank=True, default='vid/brillos.mp4')



    def __str__(self):
        return f"{self.nombre}"    

