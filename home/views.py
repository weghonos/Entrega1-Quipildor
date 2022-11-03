from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect, render
from home.forms import BusquedaFormulario, UsuarioFormulario

from home.models import Usuario


def index(request):
    return render(request, 'home/index.html')

def crear_usuario(request):

    if request.method == 'POST':

        formulario = UsuarioFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            nombre = data['nombre']
            apellido = data['apellido']
            edad = data['edad']
            fecha_nacimiento = data.get("fecha_nacimiento")
            if not fecha_nacimiento:
                fecha_nacimiento = datetime.now()

            persona = Usuario(nombre=nombre, apellido=apellido, edad=edad, fecha_nacimiento=fecha_nacimiento)
            persona.save()

        return redirect('ver_usuarios')
    

    formulario = UsuarioFormulario()
    return render(request, 'home/crear_usuario.html', {"formulario": formulario})

def ver_usuarios(request):
    
    nombre = request.GET.get('nombre', None)

    if nombre:
        usuarios = Usuario.objects.filter(nombre__icontains=nombre)
    else:
        usuarios = Usuario.objects.all()

    formulario = BusquedaFormulario()

    return render(request, 'home/ver_usuarios.html', {"usuarios": usuarios, 'formulario': formulario})

def acerca_de(request):
    return render(request, 'home/acerca_de.html')
