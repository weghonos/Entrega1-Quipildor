from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField(auto_now_add=True, null=False)

    def __str__(self):
        return f'{self.nombre}{self.apellido}'