from django.forms.fields import ChoiceField
from django.forms.widgets import Select
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserForms(UserCreationForm):

    email = forms.EmailField()
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
    username = forms.CharField(label='Nombre de usuario')
    #Clase para agregar mas campos, la cantidad de campos y sus nombres se puede ver en ADMIN
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')
        help_texts = {k:"" for k in fields}
    


