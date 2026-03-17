from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Tarea(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    data_completed = models.DateTimeField(blank=True, null=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.user.username}"
