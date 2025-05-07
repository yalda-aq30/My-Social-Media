from django.db import models

# Create your models here.

class authentication(models.Model):
    username = models.CharField(max_length=100)
    password = models.int