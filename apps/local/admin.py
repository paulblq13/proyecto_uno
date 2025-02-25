from django.contrib import admin
from apps.local.models import Cliente, FacturaEgreso, FacturaEgresoDetalle, FacturaIngreso, FormaPago, FacturaIngresoDetalle, Persona, Stock, Articulo, Categoria, Deposito, UnidadMedida, VentaFormaPago

class stockAdmin(admin.ModelAdmin):
    list_display = ('cod_articulo', 'cantidad',)
    search_fields = ('cod_articulo', 'cod_deposito',)

admin.site.register(Stock, stockAdmin)


class articuloAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('id', 'nombre',)

admin.site.register(Articulo, articuloAdmin)

class categoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('id', 'nombre',)

admin.site.register(Categoria, categoriaAdmin)

class depositoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('id', 'nombre',)

admin.site.register(Deposito, depositoAdmin)

class unidadmedidaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('id', 'nombre',)

admin.site.register(UnidadMedida, unidadmedidaAdmin)


class facturaingresoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'numero',)
    search_fields = ('id', 'numero',)

admin.site.register(FacturaIngreso, facturaingresoAdmin)

class ingresosAdmin(admin.ModelAdmin):
    list_display = ('cod_factura', 'cod_articulo', 'cantidad',)
    search_fields = ('id', 'cod_factura',)

admin.site.register(FacturaIngresoDetalle, ingresosAdmin)

class facturaegresoAdmin(admin.ModelAdmin):
    list_display = ('numero_factura',)
    search_fields = ('id', 'numero_factura',)

admin.site.register(FacturaEgreso, facturaegresoAdmin)

class facturaegresoDetalleAdmin(admin.ModelAdmin):
    list_display = ('cod_articulo', 'cantidad',)
    search_fields = ('id',)

admin.site.register(FacturaEgresoDetalle, facturaegresoDetalleAdmin)

class formapagoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('id', 'nombre',)

admin.site.register(FormaPago, formapagoAdmin)

class ventaformapagoAdmin(admin.ModelAdmin):
    list_display = ('cod_formapago', 'cod_facturaegreso',)
    search_fields = ('id', 'cod_formapago', 'cod_facturaegreso',)

admin.site.register(VentaFormaPago, ventaformapagoAdmin)

class personaAdmin(admin.ModelAdmin):
    list_display = ('apenom', 'dni',)
    search_fields = ('id', 'apenom', 'dni',)

admin.site.register(Persona, personaAdmin)

class clienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'cod_persona',)
    search_fields = ('id', 'cod_persona__apenom',)

admin.site.register(Cliente, clienteAdmin)