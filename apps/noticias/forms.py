from django import forms
from apps.noticias.models import Noticia
from django.db.models import Q

#---------------------------------------------NOTICIA FORM---------------------------
class NoticiasForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super(NoticiasForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'