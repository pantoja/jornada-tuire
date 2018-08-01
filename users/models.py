from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    picture = models.ImageField('Foto de Perfil', default='/img/blank-pic.png')
    following = models.ManyToManyField('self', blank="True")