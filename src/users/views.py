from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm
from .models import CustomUser
# Create your views here.

def profile_view(request, username):
    obj = get_object_or_404(CustomUser, username=username)
    template_name= 'user/profile.html'
    context = {
        'user': obj,
        'followers': obj.users_followers.all(),
        }
    return render(request, template_name, context)