from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def profile_view(request, username):
    logged_user    = request.user
    profile_user   = get_object_or_404(CustomUser, username=username)
    template_name  = 'user/profile.html'
    is_post_method = request.method == 'POST'
    
    if is_post_method and profile_user not in logged_user.following.all() and profile_user.username is not logged_user.username:
        print(f'adding {profile_user.full_name} to {logged_user.full_name} following list')
        logged_user.following.add(profile_user)
        print(f'adding {logged_user.full_name} to {profile_user.full_name} followers list')
        profile_user.followers.add(logged_user)
    #     print(f'{logged_user.username} is following => {logged_user.following.all()}\n and being followed by {logged_user.followers.all()}\n')
    #     print(f'{profile_user.username} is following => {profile_user.following.all()}\n and being followed by {profile_user.followers.all()}\n')
    elif is_post_method and profile_user in logged_user.following.all() and profile_user.username is not logged_user.username:
        logged_user.following.remove(profile_user)
        profile_user.followers.remove(logged_user)
        # print(f'{logged_user.username} is following => \n{logged_user.following.all()}\n and being followed by {logged_user.followers.all()}\n')
        # print(f'{profile_user.username} is following => \n{profile_user.following.all()}\n and being followed by {profile_user.followers.all()}\n')
    
    context = {
        'user'     : profile_user,
        'followers': profile_user.followers.all(),
        'following': profile_user.following.all(),
        }

    return render(request, template_name, context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

    return render(request, 'login.html', {})