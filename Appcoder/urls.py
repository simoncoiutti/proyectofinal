from django.urls import path
from Appcoder.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", inicio, name="inicio"),
    path("acerca_de/", acerca_de, name="acerca_de"),
    path("inicio", inicio, name="inicio"),
    path("acerca_de/", acerca_de , name="acerca_de"),
    path("register/", register, name="register"),
    path("login/", login_request, name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('editarPerfil/',editarPerfil, name= 'editarPerfil'),
]