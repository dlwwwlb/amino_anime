from django.db import models

# Create your models here.
# users/models.py
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='default.jpg')
    bio = models.TextField(max_length=500, blank=True)
    favorite_anime = models.CharField(max_length=100, blank=True)
    # можно добавить подписки, рейтинг и т.д.