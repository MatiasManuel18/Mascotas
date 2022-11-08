from django.contrib import admin
from .models import Mascotas, Productos
from django.utils.html import format_html
from django.utils.functional import keep_lazy, keep_lazy_text

class MascotasAdmin(admin.ModelAdmin):
    #Lista todos los datos
    list_display = ('id','titulo','foto','sexo','telefono','descripcion','fechaActual')

    #Buscar los datos
    search_fields = ('titulo',)

    #Edita la columna que quieras editar
    #list_editable = ('titulo',)

    #------Añade un hipervinculo para poder editar
    list_display_links = ('titulo',)

    #----Crea un filtro para buscar por tipos
    list_filter=('sexo',)

    #---Lista por numero que se muestra en la pantalla
    #list_per_page = 10

    def imagen(self, obj):
        return format_html('<img src={} />', obj.imagen.url)
    
    def foto(self, obj):
        return format_html('<img src={} width="130" heigth="100"/>', obj.imagen.url)
      

class ProductosAdmin(admin.ModelAdmin):
    #Lista todos los datos
    list_display = ('id','titulo','foto','precio')

    #Buscar los datos
    search_fields = ('titulo',)

    #Edita la columna que quieras editar
    #list_editable = ('titulo',)

    #------Añade un hipervinculo para poder editar
    list_display_links = ('titulo',)

    #----Crea un filtro para buscar por tipos
    list_filter=('precio',)

    #---Lista por numero que se muestra en la pantalla
    #list_per_page = 10
    def foto(self, obj):
        return format_html('<img src={} width="130" heigth="100"/>', obj.imagen.url)

# Register your models here.
admin.site.register(Mascotas, MascotasAdmin)
admin.site.register(Productos, ProductosAdmin)