from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Usuario(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()
    profesion= models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"



class Avatar(models.Model):
    imagen= models.ImageField(upload_to="avatars")
    user=models.ForeignKey(User, on_delete=models.CASCADE)




class Categoria(models.Model):
    nombre= models.CharField(max_length=30,unique=True)


class Post(models.Model):
    titulo= models.CharField(max_length=200, verbose_name='Titulo')
    bajada= models.CharField(max_length=500, verbose_name='Bajada')
    contenido= models.TextField(verbose_name= 'Contenido')
    imagen= models.ImageField(upload_to= 'Post', null=True, blank=True,verbose_name='Imagen')
    """categoria= models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name= 'Autor')"""
    creado= models.DateTimeField(auto_now_add=True,verbose_name= 'Fecha de creacion')

    class Meta:
        verbose_name= 'Publicacion'
        verbose_name_plural= 'Publicaciones'
        

    def __str__(self):
        return self.titulo



