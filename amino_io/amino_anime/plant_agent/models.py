from django.db import models
from django.contrib.auth.models import User


class Plant(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='plants')
    water_every_days = models.PositiveIntegerField(default=7)
    last_watered = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name
