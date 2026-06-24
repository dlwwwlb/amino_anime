from django.db import models
from django.contrib.auth.models import User

class Community(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    icon = models.ImageField(upload_to='community_icons/', default='community_default.jpg')
    background_image = models.ImageField(upload_to='community_backgrounds/', blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_communities')
    members = models.ManyToManyField(User, through='Membership', related_name='communities')
    created_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    tags = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    def user_role(self, user):
        if not user.is_authenticated:
            return None
        membership = self.membership_set.filter(user=user).first()
        return membership.role if membership else None

    def is_admin(self, user):
        return self.user_role(user) == 'admin'

class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)
    role = models.CharField(
        max_length=20,
        choices=[('member', 'Участник'), ('moderator', 'Модератор'), ('admin', 'Админ')],
        default='member'
    )

    def __str__(self):
        return f'{self.user.username} in {self.community.name}'