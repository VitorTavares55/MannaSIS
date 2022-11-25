from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div
from .models import Member

class CustomMemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['foto', 'nome', 'categoria', 'bolsa', 'instituicao', 'email', 'fone', 'git', 'cpf', 'rg', 'sexo', 'formacao', 'dtnasc', 'endereco', 'projeto', 'premio', 'nomeBanco', 'numeroBanco', 'numeroAgencia', 'numeroConta', 'termoCompromisso']
        widgets = {
            "dtnasc": forms.DateInput()
        }

        

class MemberForm(forms.Form):

    CATEGORIA_CHOICES = (
        (1, 'Pesquisador(a)'),
        (2, 'Aluno(a) de Iniciação Científica'),
        (3, 'Extensionista'),
    )

    BOLSA_CHOICES = (
        (1, 'Pesquisa e Extensão'),
        (2, 'Iniciação Científica'),
    )

    INSTITUICAO_CHOICES = (
        (1, 'IFPR - Campus Paranavaí'),
        (2, 'UEM - Universidade Estadual de Maringá'),
    )

    SEXO_CHOICES = (
        (1, 'Masculino'),
        (2, 'Feminino'),
        (3, 'Outro'),
    )

    FORMACAO_CHOICES =(
        (1, 'Técnico Profissionalizante'),
        (2, 'Graduado'),
        (3, 'Pós-Graduado'),
        (4, 'Mestre'),
        (5, 'Doutor(a)'),
    )

    PROJETO_CHOICES = (
        (1, 'MannaSIS'),
        (2, 'Otto'),
    )

    PREMIO_CHOICES = (
        (1, 'Menção Honrosa'),
        (2, 'Condecoração'),
    )

    foto = forms.ImageField()
    nome = forms.CharField()
    categoria = forms.ChoiceField(choices=CATEGORIA_CHOICES)
    bolsa = forms.ChoiceField(choices=BOLSA_CHOICES)
    instituicao = forms.ChoiceField(choices=INSTITUICAO_CHOICES)
    email = forms.EmailField()
    fone = forms.CharField()
    git = forms.CharField()
    cpf = forms.CharField()
    rg = forms.CharField()
    sexo = forms.ChoiceField(choices=SEXO_CHOICES)
    formacao = forms.ChoiceField(choices=FORMACAO_CHOICES)
    dtnasc = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}))
    endereco = forms.CharField()
    projeto = forms.ChoiceField(choices=PROJETO_CHOICES)
    premio = forms.ChoiceField(choices=PREMIO_CHOICES)
    nomeBanco = forms.CharField()
    numeroBanco = forms.IntegerField()
    numeroAgencia = forms.IntegerField()
    numeroConta = forms.IntegerField()
    termoCompromisso = forms.FileField()


