from django import forms
from .models import Mascotas, Productos
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FormularioContacto(forms.Form):
    nombre=forms.CharField(label='Nombre', required=True, max_length=20)
    email=forms.CharField(label='Email', required=True, max_length=30)
    telefono=forms.CharField(label='Telefono', required=True, max_length=20)
    asunto=forms.CharField(label='Asunto', required=True, max_length=20)
    contenido=forms.CharField(label='Contenido', max_length=400, widget=forms.Textarea )
   


class MascotasForm(forms.ModelForm):
    class Meta:
        model = Mascotas
        fields = '__all__'
class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'

#Funcion Registrar usuario
class UserRegisterForm(UserCreationForm):
	#email = forms.EmailField()
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']
		help_texts = {k:"" for k in fields }
  
