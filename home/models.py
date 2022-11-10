from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.conf import settings


class Post(models.Model):
    titulo = models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=30)
    fecha_creacion = models.DateField(null=True,auto_now_add=True)
    contenido = RichTextField(null=True)
    imagen = models.ImageField(upload_to='imagenes/',null=True, blank=True)
    #autor = models.ForeignKey(User(), on_delete=models.CASCADE, null=True)
    
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f'Titulo: {self.titulo} - Subtitulo: {self.subtitulo}'