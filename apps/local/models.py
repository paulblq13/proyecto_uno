from django.db import models
from django.utils import timezone
#===CLOUDNARY===
from cloudinary.models import CloudinaryField
#===CLOUDNARY===

def get_upload_folder(instance):
    # Verifica que el evento tenga un código; si no, utiliza una carpeta por defecto
    return f"local/productos/"
   
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    observacion = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.nombre}"    
      

class UnidadMedida(models.Model):
    nombre = models.CharField(max_length=100)
    observacion = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.nombre}"   


class Articulo(models.Model):
    cod_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    cod_unidad = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE, null=True, blank=True)
    capacidad = models.IntegerField(null=True, blank=True, default=1)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    observacion = models.CharField(max_length=200, null=True, blank=True)
    codigo = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return f"{self.nombre}"
    

class Deposito(models.Model):
    nombre = models.CharField(max_length=50, null=True, blank=True)
    ubicacion = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre}"    



class Stock(models.Model):
    cod_articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, null=True, blank=True)
    cod_deposito = models.ForeignKey(Deposito, on_delete=models.CASCADE, null=True, blank=True)
    cantidad = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return f"{self.nombre}"    