from django.db import models
from ckeditor.fields import RichTextField


class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    descripcion = RichTextField(null=True)
    imagen = models.ImageField(upload_to='imagen',null=True, blank=True)

    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido}'