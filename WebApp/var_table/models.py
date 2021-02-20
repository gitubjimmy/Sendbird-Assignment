from django.db import models

class Variables(models.Model):
    name = models.CharField(max_length=100)
    value = models.TextField()
