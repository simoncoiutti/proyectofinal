from django.shortcuts import render

from django.http import HttpResponse
from .models import Post,Categoria,Avatar


from Appcoder.forms import *
from django.contrib.auth.models import User #este es el nuevo
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def inicio(request):
    post = Post.objects.filter(estado = True)
    print(post)
    return render(request, "Appcoder/inicio.html",{'post':post})

#def detallePost(request,titulo):
    #post= Post.objets.get(titulo = titulo)
    #return render(request,'post.html')





def acerca_de(request):
    return render (request, "Appcoder/acerca_de.html")


def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        avatar=lista[0].imagen.url
    else:
        avatar="/media/avatars/avatarpordefecto.png"
    return avatar

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
        return render(request, "Appcoder/register.html", {"form": form})

    
        









def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usu=info["username"]
            clave=info["password"]
            user=authenticate(username=usu, password=clave)
            if user is not None:
                login(request, user)
                return render(request, "Appcoder/inicio.html", {"mensaje":f"Usuario {usu} logueado correctamente"})
            else:
                return render(request, "Appcoder/login.html", {"form": form, "mensaje":"Usuario o contrase??a incorrectos"})
        else:
            return render(request, "Appcoder/login.html", {"form": form, "mensaje":"Usuario o contrase??a incorrectos"})
    else:
        form=AuthenticationForm()
        return render(request, "Appcoder/login.html", {"form": form})


@login_required
def editarPerfil(request):
    usuario=request.user

    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()
            return render(request, "Appcoder/inicio.html", {"mensaje":f"Usuario {usuario.username} editado correctamente"})
        else:
            return render(request, "Appcoder/editarPerfil.html", {"form": form, "nombreusuario":usuario.username})
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "Appcoder/editarPerfil.html", {"form": form, "nombreusuario":usuario.username})



def agregarAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatar.save()
            return render(request, "Appcoder/inicio.html", {"mensaje":f"Avatar agregado correctamente"})
        else:
            return render(request, "Appcoder/agregarAvatar.html", {"form": form, "usuario": request.user, "mensaje":"Error al agregar el avatar"})
    else:
        form=AvatarForm()
        return render(request, "Appcoder/agregarAvatar.html", {"form": form, "usuario": request.user})

@login_required
def leerUsuarios(request):

    usuarios=User.objects.all() #aca va user.objects


    

    return render(request, "Appcoder/Usuarios.html", {"usuarios": usuarios, "avatar": obtenerAvatar(request)})



@login_required
def buscar(request):
    usuario= User.objects.all()
    
    if usuario!="":
        usuario= User.objects.all#buscar otros filtros en la documentacion de django
        return render(request, "Appcoder/resultadosBusqueda.html", {"usuarios": User})
    else:
        return render(request, "Appcoder/busquedaComision.html", {"mensaje": "Che Ingresa una comision para buscar!"})
