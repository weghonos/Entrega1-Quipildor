from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

class RegistroFormulario(UserCreationForm):
    email = forms.CharField()
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput,max_length=30)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput, max_length=30)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {key:"" for key in fields}

class EditarPerfilFormulario(forms.Form):
    email = forms.CharField()
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    avatar = forms.ImageField(required=False)


class CambiarPassword(PasswordChangeForm):
    old_password = forms.CharField(label='Contraseña actual', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='Contraseña nueva', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Repetir Contraseña nueva', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        help_texts = {key:"" for key in fields}
