from django.shortcuts import render
from home.models import Usuario
from home.forms import BusquedaUsuario

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return render(request, 'home/index.html')

def acerca_de(request):
    return render(request, 'home/acerca_de.html')

class VerUsuarios(LoginRequiredMixin,ListView):
    model = Usuario
    template_name = 'home/ver_usuarios.html'

    def get_queryset(self):
        nombre = self.request.GET.get('nombre', '')
        if nombre:
            object_list = self.model.objects.filter(nombre__icontains=nombre)
        else:
            object_list = self.model.objects.all()
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formulario"] = BusquedaUsuario()
        return context

class CrearUsuarios(LoginRequiredMixin,CreateView):
    model = Usuario
    success_url = '/usuarios/'
    template_name = 'home/crear_usuario.html'
    #fields = ['nombre','apellido','edad','fecha_nacimiento', 'descripcion']
    fields = ['nombre','apellido','edad','fecha_nacimiento','descripcion','imagen']

class EditarUsuarios(LoginRequiredMixin, UpdateView):
    model = Usuario
    success_url = '/usuarios/'
    template_name = 'home/editar_usuario.html'
    fields = ['nombre','apellido','edad','fecha_nacimiento','descripcion']
    
class EliminarUsuarios(LoginRequiredMixin, DeleteView):
    model = Usuario
    success_url = '/usuarios/'
    template_name = 'home/eliminar_usuario.html'

class InfoUsuarios(DetailView):
    model = Usuario
    template_name = 'home/info_usuarios.html'

class Posts(ListView):
    model = Usuario
    template_name = 'home/listado_posts.html'

    # def get_queryset(self):
    #     nombre = self.request.GET.get('nombre', '')
    #     if nombre:
    #         object_list = self.model.objects.filter(nombre__icontains=nombre)
    #     else:
    #         object_list = self.model.objects.all()
    #     return object_list

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["formulario"] = BusquedaUsuario()
    #     return context