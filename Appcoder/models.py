from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.






class Avatar(models.Model):
    imagen= models.ImageField(upload_to="avatars")
    user=models.ForeignKey(User, on_delete=models.CASCADE)




class Categoria (models.Model):
	nombre = models.CharField(max_length=200, unique=True, verbose_name='Nombre')
	activo = models.BooleanField(default=True, verbose_name='Activo')
	
	modificado = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

	class Meta:
		verbose_name = 'Categoría'
		verbose_name_plural = 'Categorías'
		
	def __str__(self):
		return self.name

class Post(models.Model):
    id= models.AutoField(primary_key= True)
    titulo= models.CharField(max_length=200, verbose_name='Titulo')
   
    subtitulo= models.CharField(max_length=500, verbose_name='Bajada')
    contenido= RichTextField()
    imagen= models.ImageField(upload_to= 'Post', null=True, blank=True,verbose_name='Imagen')
    
    creado= models.DateTimeField(auto_now_add=True,verbose_name= 'Fecha de creacion')
    estado= models.BooleanField('Publicado/No Publicado', default= True)
    class Meta:
        verbose_name= 'Post'
        verbose_name_plural= 'Posts'
        

    def __str__(self):
        return self.titulo



