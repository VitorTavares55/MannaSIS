from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.core.validators import MinLengthValidator
from .choices import *

# Create your models here.
class Member(models.Model):
    foto = models.ImageField('Foto', upload_to='static/uploads/photos/')
    nome = models.CharField('Nome Completo', max_length=50)
    categoria = models.CharField('Função',max_length=50)
    bolsa = models.CharField('Tipo de Bolsa', max_length=100)
    instituicao = models.CharField('Instituição', max_length=50)
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
    sexo = models.CharField('Sexo', max_length=50)
    formacao = models.CharField('Formação', max_length=50)
    dtnasc = models.DateField('Data de Nascimento')
    endereco = models.CharField('Endereço', max_length=200)
    projeto = models.CharField('Projeto Associado', max_length=50)
    premio = models.CharField('Prêmio Associado', max_length=50)
    nomeBanco = models.CharField('Nome do Banco', max_length=50)
    numeroBanco = models.CharField('Número do Banco', max_length=50)
    numeroAgencia = models.CharField('Número da Agência', max_length=50)
    numeroConta = models.CharField('Número da Conta', max_length=50)
    termoCompromisso = models.FileField('Termo de Compromisso', upload_to='static/uploads/termos/')
    termoCiencia = models.FileField('Termo de Ciência', upload_to='static/uploads/termos/')
    planoTrabalho = models.FileField('Plano de Trabalho', upload_to='static/uploads/termos/')
    lgpd = models.FileField('LGPD', upload_to='static/uploads/termos/')
    acesso = models.CharField(max_length=50)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return str(self.foto) + ' - ' + self.nome + ' - ' + self.categoria + ' - ' + self.instituicao + ' - ' + self.email + ' - ' + self.fone + ' - ' + self.git + ' - ' + self.lattes + ' - ' + self.link + ' - ' + self.insta + ' - ' + self.twt + ' - ' + self.face + ' - ' + self.youtube + ' - ' + self.cpf + ' - ' + self.rg + ' - ' + self.sexo + ' - ' + self.formacao + ' - ' + str(self.dtnasc) + ' - ' + self.endereco + ' - ' + self.projeto + ' - ' + self.premio + ' - ' + self.nomeBanco + ' - ' + self.numeroBanco + ' - ' + self.numeroAgencia + ' - ' + self.numeroConta + ' - ' + str(self.termoCompromisso) +  ' - ' + str(self.termoCiencia) +  ' - ' + str(self.planoTrabalho) + ' - ' + str(self.lgpd) + ' - ' + self.acesso + ' - ' + str(self.ativo)

class Institution(models.Model):
    foto = models.ImageField('Foto', upload_to='static/uploads/photos/institution')
    nome = models.CharField('Nome da Instituição', max_length=200)
    email = models.CharField('E-mail', max_length=50)
    telefone = models.CharField('Telefone(Sem pontuação)', max_length=50)
    site = models.CharField('Site', max_length=50)
    hub = models.CharField('Hub do Manna', max_length=50)
    esfera = models.IntegerField('Esfera', choices=ESFERA_CHOICES, default=1)
    endereco = models.CharField('Endereço', max_length=200)
    quantidadeAlunos = models.IntegerField('Quantidade de Alunos Relacionados ao Manna')
    descricao = models.CharField('Descrição', max_length=2000)

    def __str__(self):
        return str(self.foto) + ' - ' + self.nome + ' - ' + self.email + ' - ' + self.telefone + ' - ' + self.site + ' - ' + self.hub + ' - ' + str(self.esfera) + ' - ' + self.endereco + ' - ' + str(self.quantidadeAlunos) + ' - ' + self.descricao 

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
        return str(self.foto) + ' - ' + self.nome + ' - ' + self.sede + ' - ' + self.representante + ' - ' + self.instituicoes + ' - ' + self.participantes + ' - ' + self.conexao + ' - ' + str(self.quantidadeAlunos) + ' - ' + self.descricao 


