from django import forms
from ckeditor.fields import RichTextFormField

class PostFormulario(forms.Form):
    titulo = forms.CharField(max_length=30)
    subtitulo = forms.CharField(max_length=30)
    fecha_creacion = forms.DateField(required=False)
    imagen = forms.ImageField(required=False)
    contenido= RichTextFormField(required=False)
    #autor = forms.CharField(max_length=30)

class BusquedaPost(forms.Form):
    titulo = forms.CharField(max_length=30, required=False)
