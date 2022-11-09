from django.db import models
from ckeditor.fields import RichTextField


class Post(models.Model):
    titulo = models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=30)
    fecha_creacion = models.DateField(null=True)
    contenido = RichTextField(null=True)
    imagen = models.ImageField(upload_to='imagenes/',null=True, blank=True)
    
    

    def __str__(self):
        return f'Titulo: {self.titulo} - Subtitulo: {self.subtitulo}'