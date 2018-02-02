from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Perfil(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    imagen = models.ImageField(upload_to='images', blank=True, null=True)
   
    def __str__(self):
            return str(self.user)