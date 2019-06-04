from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from users.forms import UserForm, CustomUserCreationForm


def landing_view(request):
    form = CustomUserCreationForm(request.POST or None)
    if not request.user.is_authenticated:
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        return redirect('home_page')
    return render(request, 'land.html', {'form': form})


def login_view(request):
    form = UserForm(request.POST or None, request.FILES or None)
    if request.user.is_authenticated:
        return redirect('home_page')
    else:    
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user     = authenticate(request,username=username, password=password)
        if form.is_valid():
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home_page')
            else:
                return redirect('landing_view')
        
    return render(request, 'login.html', {'form': form})

def home_page(request):
    if request.user.is_authenticated:
        user = request.user
    context = {'user': user}
    template_name = 'home.html'
    return render(request, template_name, context)