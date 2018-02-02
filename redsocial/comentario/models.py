from django.db import models
from perfil.models import Perfil
from django.contrib.auth.models import User
from publicacion.models import Publicacion


# Create your models here.
class Comentario(models.Model):
    usuario=models.ForeignKey(User,related_name='usuario', on_delete=models.CASCADE, default="")
    respuestade=models.ForeignKey(Publicacion)
    respuesta=models.CharField(max_length=200)
    fecha=models.DateTimeField(blank=True, null=True, auto_now_add=True)
   
    def __str__(self):
        return self.respuesta