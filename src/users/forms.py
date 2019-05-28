from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email     = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder':'Email'}))
    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nome completo'}))
    username  = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nome de usuário'}))
    password  = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Senha'}))
    
    class Meta(UserCreationForm):
        model  = CustomUser
        fields = ('username', 'email')
        
    
class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model  = CustomUser
        fields = ('username', 'email')

class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    
