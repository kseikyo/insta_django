from django.contrib import admin
from django.contrib.auth import get_user_model
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

# Register your models here.


class MyAdmin(admin.ModelAdmin):
    fields = ['profile_picture', 'email', 'username', 'full_name']


admin.site.register(CustomUser, MyAdmin)
