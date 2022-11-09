from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name="index"),
    path('posts/lista', views.Posts.as_view(), name="posts"),
    path('post/', views.VerPosts.as_view(), name="ver_posts"),
    path('post/crear', views.CrearPost.as_view(), name="crear_post"),
    path('post/editar/<int:pk>', views.EditarPost.as_view(), name="editar_post"),
    path('post/eliminar/<int:pk>', views.EliminarPost.as_view(), name="eliminar_post"),
    path('post/info/<int:pk>', views.InfoPost.as_view(), name="info_post"),
    path('posts/', views.VerPosts.as_view(), name="ver_posts"),
    path('acerca_de/', views.acerca_de, name="acerca_de"),
    ]