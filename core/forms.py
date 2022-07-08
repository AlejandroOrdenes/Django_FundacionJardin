
from django import forms
from .models import Producto, Cliente
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        exclude = ('idProducto',)

class ClienteForm(forms.Form):
    nombre_cli = forms.CharField(max_length=40)
    email = forms.CharField(max_length=40)
    direccion = forms.CharField(max_length=40)
    password_cli = forms.CharField(max_length=40)
    suscripcion = forms.BooleanField()
    def clean_field(self):
        data = {
            self.cleaned_data["nombre_cli"],
            self.cleaned_data["email"],
            self.cleaned_data["direccion"],
            self.cleaned_data["password_cli"],
            self.cleaned_data["suscripcion"],
        
        }
        
        return data

class ClienteLogin(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'
        fields = ['email', 'password1']
    


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2' ]

        
