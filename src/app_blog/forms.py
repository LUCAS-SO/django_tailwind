from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nombre', 'email', 'contenido']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Tu nombre'}),
            'email': forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Tu email'}),
            'contenido': forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'Tu comentario'}),
        }