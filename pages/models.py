from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):

    name = models.CharField(max_length=50, help_text="Digite seu nome completo")
    identification = models.CharField(max_length=11, help_text="Informe seu cpf")
    state = models.CharField(max_length=100, help_text="Informe seu estado")
    city = models.CharField(max_length=100, help_text="Informe sua cidade")

    def __str__(self):
        return self.name + ' - ' + str(self.identification) + ' - ' + str(self.state) + ' - ' + str(self.city)