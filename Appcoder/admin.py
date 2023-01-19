from django.contrib import admin
from django.db import models
from .models import *

# Register your models here.

admin.site.register(Avatar)



#post
class postAdmin(admin.ModelAdmin):
    campo= ('creado')
    lista= ('Titulo', 'categoria', 'autor')