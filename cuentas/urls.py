from django.urls import path
from cuentas import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('iniciar_sesion/', views.IniciarSesion, name="iniciar_sesion"),
    path('cerrar_sesion/', LogoutView.as_view(template_name='cuentas/cerrar_sesion.html'), name="cerrar_sesion"),
    path('registrar/', views.registrar, name="registrar"),
    path('perfil/', views.perfil, name="perfil")
]

