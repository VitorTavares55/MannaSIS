from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):

    foto = models.ImageField(upload_to='static/uploads/')
    nome = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    instituicao = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fone = models.CharField(max_length=50)
    git = models.CharField(max_length=50)
    cpf = models.CharField(max_length=50)
    rg = models.CharField(max_length=50)
    sexo = models.CharField(max_length=50)
    formacao = models.CharField(max_length=50)
    dtnasc = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    projeto = models.CharField(max_length=50)
    premio = models.CharField(max_length=50)

    def __str__(self):
        return str(self.foto) + ' - ' + self.nome + ' - ' + self.categoria + ' - ' + self.instituicao + ' - ' + self.email + ' - ' + self.fone + ' - ' + self.git + ' - ' + self.cpf + ' - ' + self.rg + ' - ' + self.sexo + ' - ' + self.formacao + ' - ' + self.dtnasc + ' - ' + self.endereco + ' - ' + self.projeto + ' - ' + self.premio
