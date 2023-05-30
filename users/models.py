from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager


class Status(models.Model):

    class StatusType(models.Model):
        DIRETORIA = "Diretoria"
        LIDER = "Lider"
        MEMBRO = "Membro"
        STATUS = [
            (DIRETORIA, "Diretoria"),
            (LIDER, "Lider"),
            (MEMBRO, "Membro"),
        ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth = models.BooleanField(default=False)
    division = models.CharField(
        max_length=50,
        choices=StatusType.STATUS, 
        default=StatusType.MEMBRO)