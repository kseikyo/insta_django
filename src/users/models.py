from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    email     = models.EmailField(unique=True, null=False, blank=False)
    full_name = models.CharField(max_length=120, null=False, blank=False)
    username  = models.CharField(max_length=110, unique=True, null=False, blank=False)
    password  = models.CharField(max_length=40, null=False, blank=False)