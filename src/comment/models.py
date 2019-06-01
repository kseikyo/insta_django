from django.db import models
from users.models import CustomUser
from post.models import Post
# Create your models here.
class Comment(models.Model):
    owner   = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    comment = models.CharField(max_length=120)

    def __str__(self):
        return self.comment