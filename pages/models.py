from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.
class Member(models.Model):
    foto = models.ImageField('Foto', upload_to='static/uploads/photos')
    nome = models.CharField('Nome Completo', max_length=50)
    categoria = models.CharField('Função',max_length=50)
    bolsa = models.CharField('Tipo de Bolsa', max_length=100)
    instituicao = models.CharField('Instituição', max_length=50)
    email = models.CharField('E-mail', max_length=50)
    fone = models.CharField('Celular', max_length=50)
    git = models.CharField('Usuário Git', max_length=50)
    cpf = models.CharField('CPF', max_length=50)
    rg = models.CharField('RG', max_length=50)
    sexo = models.CharField('Sexo', max_length=50)
    formacao = models.CharField('Formação', max_length=50)
    dtnasc = models.CharField('Data de Nascimento', max_length=50)
    endereco = models.CharField('Endereço', max_length=50)
    projeto = models.CharField('Projeto Associado', max_length=50)
    premio = models.CharField('Prêmio Associado', max_length=50)
    nomeBanco = models.CharField('Nome do Banco', max_length=50)
    numeroBanco = models.CharField('Número do Banco', max_length=50)
    numeroAgencia = models.CharField('Número da Agência', max_length=50)
    numeroConta = models.CharField('Número da Conta', max_length=50)
    termoCompromisso = models.FileField('Termo de Compromisso', upload_to='static/uploads/termos')
    acesso = models.CharField(max_length=50)

    def __str__(self):
        return str(self.foto) + ' - ' + self.nome + ' - ' + self.categoria + ' - ' + self.instituicao + ' - ' + self.email + ' - ' + self.fone + ' - ' + self.git + ' - ' + self.cpf + ' - ' + self.rg + ' - ' + self.sexo + ' - ' + self.formacao + ' - ' + self.dtnasc + ' - ' + self.endereco + ' - ' + self.projeto + ' - ' + self.premio + ' - ' + self.nomeBanco + ' - ' + self.numeroBanco + ' - ' + self.numeroAgencia + ' - ' + self.numeroConta + ' - ' + str(self.termoCompromisso) + ' - ' + self.acesso
