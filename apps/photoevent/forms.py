from django import forms
from apps.photoevent.models import Fotos, Evento
from django.db.models import Q

#---------------------------------------------PHOTOEVENT FORM---------------------------
class FotoForm(forms.ModelForm):
    class Meta:
        model = Fotos
        fields = ['mensaje', 'imagen']
        widgets = {
            'mensaje': forms.Textarea(attrs={
                'placeholder': 'Escribe tu mensaje aquí...',
                'rows': 4,
                'cols': 40,
                'class': 'form-control',
                'maxlength': 80,
                'oninput': 'actualizarContador(this)'                
            }),
            'imagen': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',        # Acepta solo archivos de imagen
                'capture': 'environment'     # Usa la cámara trasera si está disponible
            }),
        }

#---------------------------------------------EVENTO FORM---------------------------
class EventoForm(forms.ModelForm):
    fecha_evento = forms.DateField(input_formats=['%Y-%m-%d'],
                                  widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', }))    
    class Meta:
        model = Evento
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super(EventoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'        

               