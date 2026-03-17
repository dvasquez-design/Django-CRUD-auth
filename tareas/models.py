from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Tarea(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    # Stores when the task was completed. Null means the task is still pending.
    # The database column is still named 'data_completed' from older migrations.
    # We keep the field name `date_completed` in Python code for clarity, but
    # map it to the existing DB column with `db_column`.
    date_completed = models.DateTimeField(blank=True, null=True, db_column='data_completed')
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.user.username}"
