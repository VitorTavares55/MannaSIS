from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.core.validators import MinLengthValidator
from .choices import *

class Member(models.Model):
    photo = models.ImageField('Foto', upload_to='./static/uploads/photos/')
    name = models.CharField('Nome Completo', max_length=50)
    category = models.CharField('Função',max_length=50)
    bag = models.CharField('Tipo de Bolsa', max_length=100)
    institution = models.ForeignKey('Institution', on_delete=models.PROTECT, verbose_name='Instituição')
    email = models.CharField('E-mail', max_length=50)
    fone = models.CharField('Celular(Sem pontuação)', max_length=50)
    git = models.CharField('Usuário Git', max_length=50)
    lattes = models.CharField('Lattes', max_length=50)
    link = models.CharField('Linkedin', max_length=50)
    insta = models.CharField('Instagram', max_length=50)
    twt = models.CharField('Twitter', max_length=50)
    face = models.CharField('Facebook', max_length=50)
    youtube = models.CharField('Youtube', max_length=50)
    cpf = models.CharField('CPF(Sem pontuação)', max_length=11, validators=[MinLengthValidator(11)])
    rg = models.CharField('RG(Sem pontuação)', max_length=50)
    gender = models.CharField('Gênero:', choices=SEXO_CHOICES, default="Masculino", max_length=50)
    formation = models.CharField('Formação', max_length=50)
    birthday = models.DateField('Data de Nascimento')
    address = models.CharField('Endereço', max_length=200)
    project = models.CharField('Projeto Associado', max_length=50)
    award = models.CharField('Prêmio Associado', max_length=50)
    bankName = models.CharField('Nome do Banco', max_length=50)
    bankNumber = models.CharField('Número do Banco', max_length=50)
    agencyNumber = models.CharField('Número da Agência', max_length=50)
    accountNumber = models.CharField('Número da Conta', max_length=50)
    commitment = models.FileField('Termo de Compromisso', upload_to='static/uploads/termos/', blank=True)
    science = models.FileField('Termo de Ciência', upload_to='static/uploads/termos/', blank=True)
    jobPlan = models.FileField('Plano de Trabalho', upload_to='static/uploads/termos/', blank=True)
    lgpd = models.FileField('LGPD', upload_to='static/uploads/termos/', blank=True)
    acess = models.CharField(max_length=50)
    activity = models.BooleanField(default=True)

    def __str__(self):
       return self.name

class Hub(models.Model):
    photo = models.ImageField('Foto', upload_to='./static/uploads/photos/hub')
    name = models.CharField('Nome do Hub', max_length=200)
    region = models.CharField('Região do Hub', max_length=200)
    headquarter = models.CharField('Sede do Hub', max_length=50)
    representative = models.CharField('Representante Manna', max_length=50)
    institutions= models.CharField('Instituições Afiliadas', max_length=50)
    participants = models.CharField('Membros Participantes', max_length=50)
    connection = models.CharField('Colégios Atendidos', max_length=200)
    amountStudents = models.IntegerField('Quantidade de Alunos Atendidos')
    description = models.CharField('Descrição', max_length=2000)

    def __str__(self):
        return self.name
    
class Institution(models.Model):
    photo = models.ImageField('Foto', upload_to='./static/uploads/photos/institution')
    name = models.CharField('Nome da Instituição', max_length=200)
    email = models.CharField('E-mail', max_length=50)
    fone = models.CharField('Telefone(Sem pontuação)', max_length=50)
    site = models.CharField('Site', max_length=50)
    hub = models.ForeignKey('Hub',on_delete=models.PROTECT)
    sphere = models.CharField('Esfera', choices=ESFERA_CHOICES, default="Municipal", max_length=50)
    address = models.CharField('Endereço', max_length=200)
    amountStudents = models.IntegerField('Quantidade de Alunos Relacionados ao Manna')
    description= models.CharField('Descrição', max_length=2000)

    def __str__(self):
        return self.name