from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UsuarioFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    fecha_nacimiento = forms.DateField(required=False)


class RegistroFormulario(UserCreationForm):
    email = forms.CharField()
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput,max_length=30)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput, max_length=30)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {key:"" for key in fields}


class BusquedaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)