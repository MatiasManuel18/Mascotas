from pyexpat.errors import messages
from django import http
from django.shortcuts import render, redirect
from django.http import HttpResponse, response
from flask import request, request_tearing_down
from .models import Mascotas, Productos
from .forms import FormularioContacto, MascotasForm, ProductosForm
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.db.models import Q
from .forms import UserRegisterForm, UserCreationForm
#from django.contrib import messages

from django.contrib.messages import constants
from django.contrib.auth import logout
#Importamos proteccion a las URL
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.template.loader import render_to_string
#Paginas del sitio web
def inicio(request):
    return render(request,'paginas/inicio.html')
def inicio_sesion(request):
    return render(request,'paginas/inicio_sesion.html')
def contactos(request):
    return render(request,'paginas/contactos.html')
def blog(request):
    return render(request,'paginas/blog.html')


#contactar
def correo(request):

    formulario_contacto=FormularioContacto()

    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            telefono=request.POST.get("telefono")
            asunto=request.POST.get("asunto")
            contenido=request.POST.get("contenido")

            email=EmailMessage("Mensaje de Pagina web Mascota",
            "El usuario con nombre: {} /con la dirección: {} /con el asunto:{} /con telefono: {} /escribe lo siguiente:\n\n {}".format(nombre, email,asunto,telefono, contenido), 
            '',
            ["adcomkan7@gmail.com"], 
            reply_to=[email])

            try:
                email.send()
                messages.info(request, "Enviaste Exitsos Ñe")
                return redirect("correo")
            except:
                return redirect("correo")
    return render(request, "paginas/correo.html", {"correo":formulario_contacto})



# Create your views here.


#Validacion para el registro y login
def registro(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			messages.success(request, f'Usuario {username} creado')
            #Ponemos la ubicacion donde se va dirigir
			return redirect('inicio')
	else:
		form = UserRegisterForm()

	context = { 'form' : form }
	return render(request, 'paginas/registro.html', context)
#Funcion para SALIR del inicio de sesion
def logout_request(request):
    logout(request)
    messages.info(request, "Saliste exitosamente")
    return redirect ("inicio")

#--------------------------------
#PAGINA DE LA TIENDA
#--------------------------------
def tienda(request):
    busqueda = request.POST.get("buscar")
    productos = Productos.objects.all()

    if busqueda:
        productos = Productos.objects.filter(
            Q(titulo__icontains = busqueda)
        ).distinct()
    else:
        print("No se encontro la mascota")

    return render(request,'tienda/tienda.html',{"tienda":productos})

@login_required(login_url='accounts/acceder')
def ver_productos(request):
    #Obtiene todos los datos de la tabla para visualizarlos
    busqueda = request.POST.get("buscar")
    productos = Productos.objects.all().order_by('-id')

    if busqueda:
        productos = Productos.objects.filter(
            Q(titulo__icontains = busqueda)
        ).distinct()
    else:
        print("No se encontro la mascota")

    return render(request,'tienda/ver_productos.html',{"productos":productos})

@login_required(login_url='accounts/acceder')
def crear_productos(request):
    #.POST - esta obteniendo informacion
    #.Files - Esta recepcionando archivos o imagenes
    formularioProductos = ProductosForm(request.POST or None, request.FILES or None)
    if formularioProductos.is_valid():
        formularioProductos.save()
        return redirect('ver_productos')
    return render(request,'tienda/crear_productos.html',{"formularioProductos":formularioProductos})

@login_required(login_url='accounts/acceder')
def editar_productos(request, id):
    productos = Productos.objects.get(id=id)
    formularioProductos = ProductosForm(request.POST or None, request.FILES or None, instance=productos)
    if formularioProductos.is_valid() and request.method =='POST':
        formularioProductos.save()
        return redirect('tienda')
    return render(request,'tienda/editar_tienda.html', {'formularioProductos':formularioProductos})

@login_required(login_url='accounts/acceder')
def eliminar_productos(request, id):
    productos = Productos.objects.get(id=id)
    productos.delete()
    return redirect('ver_productos')

#--------------------------------------
#PAGINA DE MASCOTAS
#-----------------------------
def buscar_animales(request):
    busqueda = request.POST.get("buscar")
    mascotas = Mascotas.objects.all().order_by('-id')

    if busqueda:
        mascotas = Mascotas.objects.filter(
            Q(titulo__icontains = busqueda)
        ).distinct()
    else:
        print("No se encontro la mascota")

    return render(request,'paginas/animales.html',{"animales":mascotas})

#Paginas de la tabla mascota
@login_required(login_url='accounts/acceder')
def mascotas(request):
    #Obtiene todos los datos de la tabla para visualizarlos
    busqueda = request.POST.get("buscar")
    mascotas = Mascotas.objects.all().order_by('-id')

    if busqueda:
        mascotas = Mascotas.objects.filter(
            Q(titulo__icontains = busqueda)
        ).distinct()
    else:
        print("No se encontro la mascota")

    return render(request,'mascotas/index.html',{"mascotas":mascotas})

@login_required(login_url='accounts/acceder')
def crear_mascotas(request):
    #.POST - esta obteniendo informacion
    #.Files - Esta recepcionando archivos o imagenes
    formulario = MascotasForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('mascotas')
    return render(request,'mascotas/crear.html',{"formulario":formulario})

@login_required(login_url='accounts/acceder')
def editar_mascotas(request, id):
    mascotas = Mascotas.objects.get(id=id)
    formulario = MascotasForm(request.POST or None, request.FILES or None, instance=mascotas)
    if formulario.is_valid() and request.method =='POST':
        formulario.save()
        return redirect('mascotas')
    return render(request,'mascotas/editar.html', {'formulario':formulario})

@login_required(login_url='accounts/acceder')
def eliminar_mascotas(request, id):
    mascota = Mascotas.objects.get(id=id)
    mascota.delete()
    return redirect('mascotas')

def sendEmail(request):     
    if request.method == 'POST':
        
        emailReciber = 'adcomkan7@gmail.com'
        sexo = request.POST['formTxtSexo']
        telefono = request.POST['formTxtTelefono']
        #imagen= request.POST['formTxtImagen']
        titulo = request.POST['formTxtNombre']
        name = request.POST['formTxtName']
        direccion = request.POST['formTxtDireccion']
        asunto = request.POST['formTxtAsunto']
        message = 'Correo mandado correctamente.'
        #variables que estan en email_template.html en la carpeta templates
        template = render_to_string('email_template.html', {
            'sexo': sexo,
            'telefono':telefono,
            #'imagen':imagen,
            'titulo': titulo,
            'name': name,
            'direccion': direccion,
            'asunto':asunto,
            'message': message
            })
        email = EmailMessage(
            message,
            template,
            settings.EMAIL_HOST_USER,
            [emailReciber])
        email.fail_silently = False
        email.send()
        #messages.succes(request, 'Correo mandado correctamente.')
        #messages.add_message(request, constants.SUCCESS, 'Message')
        return render(request,'paginas/inicio.html')
       
    
    else:
        form = UserRegisterForm()
