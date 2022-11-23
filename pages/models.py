from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    foto = models.ImageField(upload_to='static/uploads/photos')
    nome = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    bolsa = models.CharField(max_length=100)
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
    nomeBanco = models.CharField(max_length=50)
    numeroBanco = models.CharField(max_length=50)
    numeroAgencia = models.CharField(max_length=50)
    numeroConta = models.CharField(max_length=50)
    termoCompromisso = models.FileField(upload_to='static/uploads/termos')
    acesso = models.CharField(max_length=50)

    def __str__(self):
        return str(self.foto) + ' - ' + self.nome + ' - ' + self.categoria + ' - ' + self.instituicao + ' - ' + self.email + ' - ' + self.fone + ' - ' + self.git + ' - ' + self.cpf + ' - ' + self.rg + ' - ' + self.sexo + ' - ' + self.formacao + ' - ' + self.dtnasc + ' - ' + self.endereco + ' - ' + self.projeto + ' - ' + self.premio + ' - ' + self.nomeBanco + ' - ' + self.numeroBanco + ' - ' + self.numeroAgencia + ' - ' + self.numeroConta + ' - ' + str(self.termoCompromisso) + ' - ' + self.acesso
