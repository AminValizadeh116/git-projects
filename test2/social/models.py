from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    photo = models.ImageField(upload_to='/media/user', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    job = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)


class Post(models.Model):
    text = models.TextField()
    published_time = models.DateTimeField(auto_now=True)

