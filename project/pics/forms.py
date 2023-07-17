from django import forms
from django.forms import ModelForm
# OVO NIJE TREBALO JER OVO DODAJE KORISNIKE U /admin 
# A TEBI JE TREBALO DA DODAS USERS sajta
#
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

from .models import User

class PicsUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'password1' : forms.PasswordInput(),
            'password2' : forms.PasswordInput(),
        }

class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': 'Email'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))

