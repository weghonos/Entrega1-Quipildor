from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name="index"),
    path('saludo/', views.saludo, name="saludo"),
    path('crear_usuario/', views.crear_usuario, name="crear_usuario"),
]