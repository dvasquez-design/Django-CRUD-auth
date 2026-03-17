from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['title', 'description', 'important']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el titulo'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe una descripcion'}),
        }