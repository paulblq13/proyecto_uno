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
                'rows': 4,  # Número de filas del textarea
                'cols': 40,  # Número de columnas del textarea
                'class': 'form-control'  # Puedes agregar clases CSS si lo necesitas
            }),
            'imagen': forms.FileInput(attrs={
                'class': 'form-control'  # Puedes agregar clases CSS si lo necesitas
            }),
        }