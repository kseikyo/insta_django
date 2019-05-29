from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from users.forms import UserForm, CustomUserCreationForm


def landing_view(request):
    form = CustomUserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/login')
    return render(request, 'base.html', {'form': form})


def login_view(request):
    form = UserForm(request.POST or None, request.FILES or None)
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user     = authenticate(request,username=username, password=password)
    if form.is_valid():
        if user is not None:
            if user.is_active:
                login(request, user)
                # return redirect('home_page')
        else:
            return redirect('landing_view')
    
    return render(request, 'login.html', {'form': form})