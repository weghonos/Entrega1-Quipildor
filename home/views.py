from django.shortcuts import render
from home.models import Post
from home.forms import BusquedaPost

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return render(request, 'home/index.html')

def acerca_de(request):
    return render(request, 'home/acerca_de.html')

class VerPosts(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'home/ver_posts.html'

    def get_queryset(self):
        nombre = self.request.GET.get('nombre', '')
        if nombre:
            object_list = self.model.objects.filter(nombre__icontains=nombre)
        else:
            object_list = self.model.objects.all()
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formulario"] = BusquedaPost()
        return context

class CrearPost(LoginRequiredMixin,CreateView):
    model = Post
    success_url = '/posts/'
    template_name = 'home/crear_post.html'
    #fields = ['nombre','apellido','edad','fecha_nacimiento', 'descripcion']
    fields = ['titulo','subtitulo','fecha_creacion','imagen','contenido']

class EditarPost(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = '/posts/'
    template_name = 'home/editar_post.html'
    fields = ['titulo','subtitulo','fecha_creacion','imagen','contenido']
    
class EliminarPost(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/posts/'
    template_name = 'home/eliminar_post.html'

class InfoPost(DetailView):
    model = Post
    template_name = 'home/info_post.html'

class Posts(ListView):
    model = Post
    template_name = 'home/listado_posts.html'