from django.shortcuts import redirect, render

from home.forms import BusquedaFormulario, UsuarioFormulario, RegistroFormulario
from home.models import Usuario

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'home/index.html')

@login_required
def crear_usuario(request):

    if request.method == 'POST':

        formulario = UsuarioFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            usuario = Usuario(
            nombre = data['nombre'],
            apellido = data['apellido'],
            edad = data['edad'],
            fecha_nacimiento = data['fecha_nacimiento']
            )
            
            usuario.save()
            return redirect('ver_usuarios')

        else:
            return render(request, 'home/editar_usuario.html', {"formulario": formulario})
 
    formulario = UsuarioFormulario()
    return render(request, 'home/crear_usuario.html', {"formulario": formulario})

@login_required
def ver_usuarios(request):
    
    nombre = request.GET.get('nombre', None)

    if nombre:
        usuarios = Usuario.objects.filter(nombre__icontains=nombre)
    else:
        usuarios = Usuario.objects.all()

    formulario = BusquedaFormulario()

    return render(request, 'home/ver_usuarios.html', {"usuarios": usuarios, 'formulario': formulario})

@login_required
def editar_usuario(request, id):

    usuario = Usuario.objects.get(id=id)

    if request.method == 'POST':

        formulario = UsuarioFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            usuario.nombre = data['nombre']
            usuario.apellido = data['apellido']
            usuario.edad = data['edad']
            usuario.fecha_nacimiento = data['fecha_nacimiento']

            usuario.save()
            return redirect('ver_usuarios')  
    

    formulario = UsuarioFormulario(
        initial={
            'nombre': usuario.nombre,
            'apellido': usuario.apellido,
            'edad': usuario.edad, 
            'fecha_nacimiento': usuario.fecha_nacimiento
        }
    )
    return render(request, 'home/editar_usuario.html', {"formulario": formulario, 'usuario': usuario})

@login_required
def eliminar_usuario(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return redirect('ver_usuarios')

def acerca_de(request):
    return render(request, 'home/acerca_de.html')


class VerUsuarios(LoginRequiredMixin,ListView):
    model = Usuario
    template_name = 'home/ver_usuarios.html'

class CrearUsuarios(LoginRequiredMixin,CreateView):
    model = Usuario
    success_url = '/usuarios/'
    template_name = 'home/crear_usuario.html'
    fields = ['nombre','apellido','edad','fecha_nacimiento']

class EditarUsuarios(UpdateView,LoginRequiredMixin):
    model = Usuario
    success_url = '/usuarios/'
    template_name = 'home/editar_usuario.html'
    fields = ['nombre','apellido','edad','fecha_nacimiento']
    
class EliminarUsuarios(DeleteView,LoginRequiredMixin):
    model = Usuario
    success_url = '/usuarios/'
    template_name = 'home/eliminar_usuario.html'