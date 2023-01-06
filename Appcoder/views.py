from django.shortcuts import render
from .models import *
from django.http import HttpResponse

def inicio(request):
    return render (request, "Appcoder/inicio.html")


def acerca_de_mi(request):
    return HttpResponse("A ver si anda")
# Create your views here.
