from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.conf import settings


class Camaron(models.Model):
    especie = models.CharField(max_length=30)
    variedad = models.CharField(max_length=30)
    temperatura = models.CharField(max_length=30)
    ph = models.CharField(max_length=30)
    fecha_creacion = models.DateField(null=True,auto_now_add=True)
    contenido = RichTextField(null=True)
    imagen = models.ImageField(upload_to='imagenes/',null=True, blank=False)
    autor = models.ForeignKey(User(), on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Especie: {self.especie} - Variedad: {self.variedad} - Autor: {self.autor}'