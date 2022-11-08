from distutils.command.upload import upload
from tkinter import image_names
from tokenize import blank_re
from django.db import models
from django.utils import timezone

# Create your models here.
class Mascotas(models.Model):
    #Hacemos que el id sea autoincremental
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=40,verbose_name="Titulo", help_text="Titulo de la mascota")
    imagen = models.ImageField(upload_to='imagenes/',verbose_name="Imagen",null=True)
    sexo = models.CharField(max_length=10,verbose_name="Sexo",null=True)
    telefono = models.CharField(max_length=9,verbose_name="Telefono",null=True)
    descripcion = models.TextField(verbose_name="Descripcion",null=True)
    fechaActual = models.DateField(default=timezone.now, verbose_name="Fecha de la publicacion")
class Productos(models.Model):
    #Hacemos que el id sea autoincremental
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100,verbose_name="Titulo", help_text="Titulo del producto")
    imagen = models.ImageField(upload_to='imagenes/',verbose_name="Imagen",null=True)
    precio = models.CharField(max_length=10, verbose_name="Precio")
    #precio = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Precio",null=True)

    #Remplaza el lugar_objetc 1 por el titulo que pusimos
    def __str__(self):
        datos = "Titulo: " + self.titulo
        return datos
    #Borra automaticamente la imagen de la carpeta "/imagenes"
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
