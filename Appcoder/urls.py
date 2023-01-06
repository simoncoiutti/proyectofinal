from django.urls import path
from Appcoder.views import *



urlpatterns = [
    path("", inicio, name="inicio"),
    path('acerca/', acerca_de_mi),
]