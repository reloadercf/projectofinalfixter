from django.db import models
from perfil.models import Perfil
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Publicacion(models.Model):
    user=models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    texto=models.CharField(max_length=200)
    fecha=models.DateTimeField(blank=True, null=True, auto_now_add=True)
   
    def __str__(self):
        return str(self.texto)