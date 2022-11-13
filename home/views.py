from django.shortcuts import render
from home.models import Camaron
from home.forms import BusquedaPost, PostFormulario

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return render(request, 'home/index.html')

def acerca_de(request):
    return render(request, 'home/acerca_de.html')

class VerPosts(ListView):
    model = Camaron
    template_name = 'home/buscar_posts.html'

    def get_queryset(self):
        especie = self.request.GET.get('especie', '')
        if especie:
            object_list = self.model.objects.filter(especie__icontains=especie)
        else:
            object_list = self.model.objects.all()
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formulario"] = BusquedaPost()
        return context

class CrearPost(LoginRequiredMixin,CreateView):
    model = Camaron
    success_url = '/posts/'
    template_name = 'home/crear_post.html'
    fields = ['especie','variedad', 'temperatura', 'ph', 'imagen','contenido']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class EditarPost(LoginRequiredMixin, UpdateView):
    model = Camaron
    success_url = '/posts/'
    template_name = 'home/editar_post.html'
    fields = ['especie','variedad', 'temperatura', 'ph', 'imagen','contenido']
    
class EliminarPost(LoginRequiredMixin, DeleteView):
    model = Camaron
    success_url = '/posts/'
    template_name = 'home/eliminar_post.html'

class InfoPost(DetailView):
    model = Camaron
    template_name = 'home/info_post.html'

class Posts(ListView):
    model = Camaron
    template_name = 'home/ver_posts.html'