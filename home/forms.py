from django import forms
from ckeditor.fields import RichTextFormField

class PostFormulario(forms.Form):
    especie = forms.CharField(max_length=30)
    variedad = forms.CharField(max_length=30)
    imagen = forms.ImageField(required=False)
    temperatura = forms.CharField(max_length=30)
    ph = forms.CharField(max_length=30)
    contenido= RichTextFormField(required=False)

class BusquedaPost(forms.Form):
    especie = forms.CharField(max_length=30, required=False)
