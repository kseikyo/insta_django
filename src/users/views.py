from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user     = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # redirect('home')
    else:
        redirect('login_view')