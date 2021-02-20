from django.db import models
from django.utils import timezone

class Variables(models.Model):
    name = models.CharField(max_length=100)
    value = models.TextField()
    recently_modified = models.BooleanField(default=False)
    last_modified = models.DateTimeField(default=timezone.now)
    previous = models.TextField(default=value)
