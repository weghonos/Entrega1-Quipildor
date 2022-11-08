from django import forms
from ckeditor.fields import RichTextFormField

class UsuarioFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    fecha_nacimiento = forms.DateField(required=False)
    descripcion = RichTextFormField(required=False)

    #imagen = forms.ImageField(required=False)

class BusquedaUsuario(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)
