from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio_view, name="inicio"),
    path("login/", views.login_view, name="login"),
    path("registro/", views.registro_view, name="registro"),
    path("logout/", views.logout_view, name="logout"),
    path("servicios/", views.servicios_view, name="servicios"),
    path("perfil/", views.perfil_view, name="perfil"),
]