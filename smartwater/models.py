from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    pass

class Niveles(models.Model):
    id_dispositivo = models.CharField(max_length=30, blank=True, null=True)
    nivel = models.IntegerField()
    motor = models.BooleanField(default=False)
    fuente = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
