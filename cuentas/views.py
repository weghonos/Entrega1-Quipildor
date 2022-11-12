from django.shortcuts import redirect,render

from cuentas.forms import RegistroFormulario, EditarPerfilFormulario, CambiarPassword
from django.contrib.auth.forms import AuthenticationForm
from cuentas.models import ExtensionUsuario

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import PasswordChangeView


def IniciarSesion(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            login(request, usuario)
            extensionUsuario, es_nuevo = ExtensionUsuario.objects.get_or_create(user = request.user)
            return redirect('index')
    else:
        formulario = AuthenticationForm()
    return render (request, 'cuentas/iniciar_sesion.html', {'formulario': formulario} )

def registrar( request):

    if request.method == 'POST':
        formulario = RegistroFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
    else:
        formulario = RegistroFormulario()

    return render (request, 'cuentas/registrar.html', {'formulario': formulario} )


@login_required
def perfil(request):
    return render (request, 'cuentas/perfil.html',{})

    
@login_required
def editar_perfil(request):

    if request.method == "POST":
        formulario = EditarPerfilFormulario(request.POST, request.FILES)

        if formulario.is_valid():
            data_nueva = formulario.cleaned_data
            request.user.first_name = data_nueva['first_name']
            request.user.last_name = data_nueva['last_name']
            request.user.email = data_nueva['email']
            request.user.extensionusuario.descripcion = data_nueva['descripcion']
            request.user.extensionusuario.link = data_nueva['link']
            request.user.extensionusuario.avatar = data_nueva['avatar']
            
            request.user.extensionusuario.save()
            request.user.save()
            return redirect('perfil')
    else:
        formulario = EditarPerfilFormulario(
            initial={
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'email': request.user.email,
                'descripcion': request.user.extensionusuario.descripcion,
                'link': request.user.extensionusuario.link,
                'avatar': request.user.extensionusuario.avatar,
            }
        )
    return render (request, 'cuentas/editar_perfil.html',{'formulario': formulario})

class CambiarContrasena(LoginRequiredMixin, PasswordChangeView):
    template_name = 'cuentas/cambiar_contrasena.html'
    success_url = '/cuentas/perfil'
    form_class = CambiarPassword