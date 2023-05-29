from django.contrib.auth.models import User
from django.db import models


class Status(models.Model):

    class StatusType(models.Model):
        DIRETORIA = "DIRETORIA"
        LIDER_HUB = "LIDER DE HUB"
        MEMBRO = "MEMBRO"
        STATUS = [
            (DIRETORIA, "Diretoria"),
            (LIDER_HUB, "Lider de Hub"),
            (MEMBRO, "Membro"),
        ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth = models.BooleanField(default=False)
    division = models.CharField(
        max_length=50,
        choices=StatusType.STATUS, 
        default=StatusType.MEMBRO)