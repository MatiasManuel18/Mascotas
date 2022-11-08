from unicodedata import name
from xml.dom.minidom import Document
from django.urls import URLPattern, path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.auth.views import LoginView
#Escribimos la direccion de nuestras paginas
urlpatterns = [
#Direccion de (templates/paginas/index.html)
    path('', views.inicio, name='inicio'),
    #Funcion para listar_animales
    path('animales', views.buscar_animales, name='animales'),
    path("correo", views.correo, name='correo'),
    #blog
    path('blog',views.blog,name="blog"),
    
    #Direccion de (templates/mascotas/index.html)
    path('mascotas', views.mascotas, name='mascotas'),
    path('mascotas/crear',views.crear_mascotas, name="crear_mascotas"),
    path('mascotas/editar',views.editar_mascotas, name="editar_mascotas"),
    #Manipulacion de datos del borrado y editado
    path('eliminar/<int:id>',views.eliminar_mascotas, name="eliminar_mascotas"),
    path('mascotas/editar/<int:id>',views.editar_mascotas,name="editar_mascotas"),
    #Tienda
    path('tienda',views.tienda,name="tienda"),
    path('ver_productos',views.ver_productos,name="ver_productos"),
    path('crear_productos',views.crear_productos,name="crear_productos"),
    #Manipulacion de datos del borrado y editado
    path('delete/<int:id>',views.eliminar_productos, name="eliminar_productos"),
    path('mascotas/editar_tienda/<int:id>',views.editar_productos,name="editar_productos"),
    #INICIO DE SESION
    path('registro',views.registro,name="registro"),
	path('inicio_sesion', LoginView.as_view(template_name='paginas/inicio_sesion.html'), name='inicio_sesion'),
    #logout es para salir de la sesion
    path('logout',views.logout_request,name="logout"),
      #Funcion para mandar_correo
    path('sendEmail', views.sendEmail, name='sendEmail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#path (es el http de la pagina)
#views.el nombre de la clase
#name="Nuestro link para acceder en <href>"