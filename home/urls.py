from django.urls import path
from django.contrib import admin
from home import views

urlpatterns = [
 #   path('', views.index, name="index"),
 #   path('usuarios/crear', views.crear_usuario, name="crear_usuario"),
 #   path('usuarios/editar/<int:id>', views.editar_usuario, name="editar_usuario"),
 #   path('usuarios/eliminar/<int:id>', views.eliminar_usuario, name="eliminar_usuario"),
 #   path('usuarios/', views.ver_usuarios, name="ver_usuarios"),
 #   path('acerca_de/', views.acerca_de, name="acerca_de"),

    path('', views.index, name="index"),
    path('usuarios/crear', views.CrearUsuarios.as_view(), name="crear_usuario"),
    path('usuarios/editar/<int:id>', views.EditarUsuarios.as_view(), name="editar_usuario"),
#    path('usuarios/eliminar/<int:id>', views.EliminarUsuarios.as_view(), name="eliminar_usuario"),
    path('usuarios/', views.VerUsuarios.as_view(), name="ver_usuarios"),
    path('acerca_de/', views.acerca_de, name="acerca_de"),

]