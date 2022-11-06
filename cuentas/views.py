from django.shortcuts import redirect,render

from home.forms import RegistroFormulario
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required



def IniciarSesion(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            login(request, usuario)
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