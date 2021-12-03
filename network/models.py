from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.db.models.fields import related, AutoField


class User(AbstractUser):
    pass

class UserFollowing(models.Model):
    user = models.CharField(max_length=64,default=None)
    following = models.CharField(max_length=64,default=None)   

    def __str__(self):
        return f"{self.user}"



class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField(blank=False)
    date = models.DateTimeField(default=None)
    likes = models.IntegerField(default=0) 

    def __str__(self):
        return f"{self.id}"   



class LikedPosts(models.Model):
    user = models.CharField(max_length=64)
    post = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.post}"