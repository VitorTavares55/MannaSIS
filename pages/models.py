from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.core.validators import MinLengthValidator
from .choices import *

class Hub(models.Model):
    foto = models.ImageField('Foto', upload_to='static/uploads/photos/hub')
    nome = models.CharField('Nome do Hub', max_length=200)
    regiao = models.CharField('Região do Hub', max_length=200)
    sede = models.CharField('Sede do Hub', max_length=50)
    representante = models.CharField('Representante Manna', max_length=50)
    instituicoes= models.CharField('Instituições Afiliadas', max_length=50)
    participantes = models.CharField('Membros Participantes', max_length=50)
    conexao = models.CharField('Colégios Atendidos', max_length=200)
    quantidadeAlunos = models.IntegerField('Quantidade de Alunos Atendidos')
    descricao = models.CharField('Descrição', max_length=2000)

    def __str__(self):
        return self.nome
    
class Institution(models.Model):
    foto = models.ImageField('Foto', upload_to='static/uploads/photos/institution')
    nome = models.CharField('Nome da Instituição', max_length=200)
    email = models.CharField('E-mail', max_length=50)
    telefone = models.CharField('Telefone(Sem pontuação)', max_length=50)
    site = models.CharField('Site', max_length=50)
    hub = models.ForeignKey('Hub',on_delete=models.PROTECT)
    esfera = models.IntegerField('Esfera', choices=ESFERA_CHOICES, default=1)
    endereco = models.CharField('Endereço', max_length=200)
    quantidadeAlunos = models.IntegerField('Quantidade de Alunos Relacionados ao Manna')
    descricao = models.CharField('Descrição', max_length=2000)

    def __str__(self):
        return self.nome
    
class Member(models.Model):
    foto = models.ImageField('Foto', upload_to='static/uploads/photos/')
    nome = models.CharField('Nome Completo', max_length=50)
    categoria = models.CharField('Função',max_length=50)
    bolsa = models.CharField('Tipo de Bolsa', max_length=100)
    instituicao = models.ForeignKey('Institution', on_delete=models.PROTECT, verbose_name='Instituição')
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
    genero = models.IntegerField('Gênero:', choices=SEXO_CHOICES, default=1)
    formacao = models.CharField('Formação', max_length=50)
    dtnasc = models.DateField('Data de Nascimento')
    endereco = models.CharField('Endereço', max_length=200)
    projeto = models.CharField('Projeto Associado', max_length=50)
    premio = models.CharField('Prêmio Associado', max_length=50)
    nomeBanco = models.CharField('Nome do Banco', max_length=50)
    numeroBanco = models.CharField('Número do Banco', max_length=50)
    numeroAgencia = models.CharField('Número da Agência', max_length=50)
    numeroConta = models.CharField('Número da Conta', max_length=50)
    termoCompromisso = models.FileField('Termo de Compromisso', upload_to='static/uploads/termos/', blank=True)
    termoCiencia = models.FileField('Termo de Ciência', upload_to='static/uploads/termos/', blank=True)
    planoTrabalho = models.FileField('Plano de Trabalho', upload_to='static/uploads/termos/', blank=True)
    lgpd = models.FileField('LGPD', upload_to='static/uploads/termos/', blank=True)
    acesso = models.CharField(max_length=50)
    ativo = models.BooleanField(default=True)

    def __str__(self):
       self.nome
