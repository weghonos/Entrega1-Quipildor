from django import forms

class UsuarioFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    fecha_nacimiento = forms.DateField(required=False)
    imagen = forms.ImageField(required=False)

class BusquedaUsuario(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)
