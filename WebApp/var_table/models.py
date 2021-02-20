from django.db import models

class Variables(models.Model):
    Variable_name = models.CharField(max_length=100)
    Value = models.CharField(max_length=100)
