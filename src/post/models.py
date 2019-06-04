from django.db import models
from users.models import CustomUser
from comment.models import Comment
# Create your models here.
class Post(models.Model):
    owner    = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title    = models.CharField(max_length=40)
    com = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return self.title