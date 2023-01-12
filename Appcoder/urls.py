from django.urls import path
from Appcoder.views import *



urlpatterns = [
    path("", inicio, name="inicio"),
    path("acerca_de/", acerca_de, name="acerca_de"),
    path("inicio", inicio, name="inicio"),
    path("acerca_de/", acerca_de , name="acerca_de"),
    path("register/", register, name="register"),
    
]