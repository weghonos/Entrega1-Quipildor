from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name="index"),
    path('crear_usuario/', views.crear_usuario, name="crear_usuario"),
    path('ver_usuarios/', views.ver_usuarios, name="ver_usuarios"),
    path('acerca_de/', views.acerca_de, name="acerca_de"),
]