from django.db import models
from users.models import CustomUser
# Create your models here.
class Comment(models.Model):
    owner   = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    com = models.CharField(max_length=120)

    def __str__(self):
        return self.com