from django import forms
from apps.local.models import Articulo, FacturaEgreso, FacturaEgresoDetalle


#---------------------------------------------AGREGAR ARTICULO FORM---------------------------
class ArticuloForm(forms.ModelForm):
   
    class Meta:
        model = Articulo
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super(ArticuloForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['cod_categoria'].widget.attrs.update({
            'class': 'form-control select2-categoria',         
        })  
        self.fields['cod_unidad'].widget.attrs.update({
            'class': 'form-control select2-cod_unidad',         
        })            
        

#---------------------------------------------FACTURA EGRESo FORM---------------------------
class FacturaEgresoForm(forms.ModelForm):
   
    class Meta:
        model = FacturaEgreso
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super(FacturaEgresoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['cod_cliente'].widget.attrs.update({
            'class': 'form-control select2-cliente',         
        })                   
      

#---------------------------------------------FACTURA EGRESO DETALLE FORM---------------------------
class FacturaEgresoDetalleForm(forms.ModelForm):
   
    class Meta:
        model = FacturaEgresoDetalle
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super(FacturaEgresoDetalle, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['cod_articulo'].widget.attrs.update({
            'class': 'form-control select2-articulo',         
        })                     