from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

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

    class Meta:
        model = CustomUser
