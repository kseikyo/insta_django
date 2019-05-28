from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm
# Create your views here.

def login_view(request):
    form = UserForm(request.POST or None, request.FILES or None)
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user     = authenticate(request, username=username, password=password)
    if form.is_valid():
        if user is not None:
            login(request, user)
            # redirect('home')
        else:
            return redirect('home_page')
    
    return render(request, 'user/login.html', {'form': form})