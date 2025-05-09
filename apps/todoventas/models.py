from django.utils import timezone
from django.db import models

class Categorias(models.Model):
    nombre = models.CharField(max_length=50, null=True, blank=True)
    observacion = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre}"
    
class Depositos(models.Model):
    nombre = models.CharField(max_length=100, null=True, blank=True)
    descripcion = models.CharField(max_length=100, null=True, blank=True)
    piso = models.IntegerField(null=True)
    ubicacion = models.CharField(max_length=500, null=True, blank=True)
    direccion = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = "Depósito"
        verbose_name_plural = "Depósitos"

    def __str__(self):
        return f"{self.nombre}"  
    
class Personas(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150, blank=True, null=True)
    dni = models.IntegerField(null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    correo_electronico = models.EmailField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Proveedores(models.Model):
    nombre = models.CharField(max_length=150)
    responsable = models.CharField(max_length=150, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    correo_electronico = models.EmailField(blank=True, null=True)
    creado_el = models.DateTimeField(default=timezone.now)
    creado_por = models.ForeignKey(Personas, on_delete=models.CASCADE, null=True, blank=True, related_name='proveedores_personas_a')
    modificado_el = models.DateTimeField(default=timezone.now)
    modificado_por = models.ForeignKey(Personas, on_delete=models.CASCADE, null=True, blank=True, related_name='proveedores_personas_b')
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"    
    
    def __str__(self):
        return self.nombre


class Productos(models.Model):
    id_categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    id_proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150, null=True, blank=True)
    detalle = models.CharField(max_length=1000, null=True, blank=True)
    estado = models.BooleanField(default=True)
    observacion = models.CharField(max_length=300, null=True, blank=True)
    precio_costo = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    precio_mayorista = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    creado_el = models.DateTimeField(default=timezone.now)
    creado_por = models.ForeignKey(Personas, on_delete=models.CASCADE, null=True, blank=True, related_name='productos_personas_a')
    modificado_el = models.DateTimeField(default=timezone.now)
    modificado_por = models.ForeignKey(Personas, on_delete=models.CASCADE, null=True, blank=True, related_name='productos_personas_b')
    serializado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre}"
    
    
class ProductoUnico(models.Model):
    id_producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    serial = models.CharField(max_length=30, null=True)
    deposito = models.ForeignKey(Depositos, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Producto Único"
        verbose_name_plural = "Productos Únicos"

    def __str__(self):
        return f"{self.serial}"  