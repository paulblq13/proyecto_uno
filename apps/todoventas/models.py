from django.db import models

class Categorias(models.Model):
    nombre = models.CharField(max_length=50, null=True, blank=True)
    observacion = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre}"
    
class Productos(models.Model):
    id_categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150, null=True, blank=True)
    detalle = models.CharField(max_length=1000, null=True, blank=True)
    estado = models.CharField(max_length=1000, null=True, blank=True)
    observacion = models.CharField(max_length=300, null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    actualizado = models.DateTimeField()
    serial = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre}"    