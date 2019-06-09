from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    id              = models.AutoField(auto_created=True, primary_key=True, serialize=True, verbose_name='ID')
    profile_picture = models.ImageField(upload_to='images/', default='/static/images/default_profile.jpeg')
    followers       = models.ManyToManyField("self", blank=True, related_name='users_following', symmetrical=False)
    following       = models.ManyToManyField("self", blank=True, related_name='users_followers', symmetrical=False)
    email           = models.EmailField(unique=True, null=False, blank=False)
    full_name       = models.CharField(max_length=120, null=False, blank=False)
    username        = models.CharField(max_length=110, unique=True, null=False, blank=False)
    password        = models.CharField(max_length=40, null=False, blank=False)

    def __str__(self):
        return self.full_name