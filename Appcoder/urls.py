from django.urls import path,include, re_path
from Appcoder.views import *
from django.contrib.auth.views import LogoutView
from os.path import os
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("", inicio, name="inicio"),
    path("acerca_de/", acerca_de, name="acerca_de"),
    path("inicio", inicio, name="inicio"),
    path("acerca_de/", acerca_de , name="acerca_de"),
    path("register/", register, name="register"),
    path("login/", login_request, name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('editarPerfil/',editarPerfil, name= 'editarPerfil'),
    path('agregarAvatar/',agregarAvatar, name= 'agregarAvatar'),
    path('usuarios/',leerUsuarios, name= 'usuarios' ),
    path('resultadoBusqueda/',buscar,name= 'resultadoBusqueda'),
    
]