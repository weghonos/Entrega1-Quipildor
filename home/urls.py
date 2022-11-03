from django.urls import path
from django.contrib import admin
from home import views

urlpatterns = [
    path('', views.index, name="index"),
    path('usuarios/crear', views.crear_usuario, name="crear_usuario"),
    path('usuarios/', views.ver_usuarios, name="ver_usuarios"),
    path('acerca_de/', views.acerca_de, name="acerca_de"),
    path('admin/', admin.site.urls),
]