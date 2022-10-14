from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
from django.shortcuts import render

from home.models import Usuario

def saludo(request):
    fecha = datetime.now()
    return HttpResponse(f"hola, hoy es: {fecha}")

def index(request):
    return render(request, 'home/index.html')

def crear_usuario(request):
    usuario = Usuario
    return render(request, 'home/crear_usuario.html')
