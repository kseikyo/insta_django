from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='images/', default='/static/images/default_profile.jpeg')
    followers       = models.ForeignKey('self', on_delete=models.CASCADE, related_name='users_followers', default=0)
    following       = models.ForeignKey('self', on_delete=models.CASCADE, related_name='users_following', default=0)
    email           = models.EmailField(unique=True, null=False, blank=False)
    full_name       = models.CharField(max_length=120, null=False, blank=False)
    username        = models.CharField(max_length=110, unique=True, null=False, blank=False)
    password        = models.CharField(max_length=40, null=False, blank=False)

    def __str__(self):
        return self.full_name