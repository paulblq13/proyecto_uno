from django.db import models
from django.utils import timezone
#===CLOUDNARY===
from cloudinary.models import CloudinaryField
#===CLOUDNARY===

def get_upload_folder(instance):
    # Verifica que el evento tenga un código; si no, utiliza una carpeta por defecto
    return f"local/productos/"
   

class Persona(models.Model):
    apenom = models.CharField(max_length=100, blank=True, null=True)
    dni = models.IntegerField(blank=True, null=True)
    telefono01 = models.CharField(max_length=50, blank=True, null=True)
    direccion= models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return f"{self.apenom}"
    
class Cliente(models.Model):
    cod_persona = models.ForeignKey(Persona, on_delete=models.CASCADE, blank=True, null=True)
    cantidad_compras = models.IntegerField(blank=True, null=True, default=0)
    observacion = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return f"{self.cod_persona}"

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    observacion = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return f"{self.nombre}"    

class UnidadMedida(models.Model):
    nombre = models.CharField(max_length=100)
    observacion = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return f"{self.nombre}"   


class Articulo(models.Model):
    cod_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    cod_unidad = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE, null=True, blank=True)
    capacidad = models.FloatField(null=True, blank=True, default=0)
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
        return f"{self.cod_articulo.nombre}"    
    
class FacturaIngreso(models.Model):
    tipo = models.CharField(max_length=2, null=True, blank=True)
    numero = models.CharField(max_length=30, null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    fecha = models.DateField()
    observacion = models.CharField(max_length=200, null=True, blank=True)
    finalizado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.numero}"
    
class FacturaIngresoDetalle(models.Model):
    cod_factura = models.ForeignKey(FacturaIngreso, on_delete=models.CASCADE, null=True, blank=True)
    cod_articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, null=True, blank=True)
    cantidad = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.cod_articulo} {self.cantidad}"
    
class FormaPago(models.Model):
    nombre = models.CharField(max_length=30, null=True, blank=True)
    observacion = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre}"
    
        
class FacturaEgreso(models.Model):
    cod_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True, null=True)
    tipo_factura = models.CharField(max_length=2, null=True, blank=True)
    numero_factura = models.CharField(max_length=30, null=True, blank=True)
    ticket = models.CharField(max_length=30, blank=True, null=True)
    fechahora = models.DateTimeField()
    presupuesto = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.numero_factura}"
    
class VentaFormaPago(models.Model):
    cod_formapago = models.ForeignKey(FormaPago, on_delete=models.CASCADE, blank=True, null=True)
    cod_facturaegreso = models.ForeignKey(FacturaEgreso, on_delete=models.CASCADE, blank=True, null=True)
    monto = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.monto}"   
    
class FacturaEgresoDetalle(models.Model):
    factura = models.ForeignKey (FacturaEgreso, on_delete=models.CASCADE, null=True, blank=True)    
    cod_articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)    
    cantidad = models.IntegerField(null=True, blank=True, default=1)
    descuento = models.IntegerField(null=True, blank=True)    

    def __str__(self):
        return f"{self.cod_articulo.nombre}"

