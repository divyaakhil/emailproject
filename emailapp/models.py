from django.db import models

# Create your models here.
class email(models.Model):
    Username = models.CharField(max_length=255,null=True)
    Password = models.CharField(max_length=255,null=True)
    Email = models.EmailField(null=True)