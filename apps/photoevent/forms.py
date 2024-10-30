from django import forms
from apps.photoevent.models import Fotos
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
                'class': 'form-control'
            }),
            'imagen': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',        # Acepta solo archivos de imagen
                'capture': 'environment'     # Usa la cámara trasera si está disponible
            }),
        }