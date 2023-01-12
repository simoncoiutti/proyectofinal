from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from Appcoder.forms import RegistroUsuarioForm

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required #para vistas basadas en funciones DEF  
from django.contrib.auth.mixins import LoginRequiredMixin #para vistas basadas en clases CLASS   


# Create your views here.
def inicio(request):
    return render (request, "Appcoder/inicio.html")

def acerca_de(request):
    return render (request, "Appcoder/acerca_de.html")


def register(request):
    if request.method=="POST":
        form= RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            form.save()
            return render(request, "Appcoder/inicio.html", {"mensaje":f"Usuario {username} creado correctamente"})
        else:
            return render(request, "Appcoder/register.html", {"form": form, "mensaje":"Error al crear el usuario"})
    else:
        form= RegistroUsuarioForm()
        return render(request, "AppCoder/register.html", {"form": form})
