from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name="index"),
    path('usuarios/', views.VerUsuarios.as_view(), name="ver_usuarios"),
    path('usuarios/crear', views.CrearUsuarios.as_view(), name="crear_usuario"),
    path('usuarios/editar/<int:pk>', views.EditarUsuarios.as_view(), name="editar_usuario"),
    path('usuarios/eliminar/<int:pk>', views.EliminarUsuarios.as_view(), name="eliminar_usuario"),
    path('usuarios/info/<int:pk>', views.InfoUsuarios.as_view(), name="info_usuario"),
    path('usuarios/', views.VerUsuarios.as_view(), name="ver_usuarios"),
    path('acerca_de/', views.acerca_de, name="acerca_de"),
    ]