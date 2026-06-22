from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    community = models.ForeignKey('communities.Community', on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    is_pinned = models.BooleanField(default=False)

    def __str__(self):
        return self.title