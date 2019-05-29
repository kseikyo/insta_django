from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email     = forms.EmailField(required=True, label='', widget=forms.TextInput(attrs={'placeholder':'Email'}))
    full_name = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'placeholder':'Nome completo'}))
    username  = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'placeholder':'Nome de usuário'}))
    password1 = forms.CharField(required=True, label='', widget=forms.PasswordInput(attrs={'placeholder':'Senha'}))
    password2 = None
    class Meta(UserCreationForm):
        model  = CustomUser
        fields = ('email', 'full_name', 'username', 'password1')
        
    
class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model  = CustomUser
        fields = ('username', 'email')

class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    
