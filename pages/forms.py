from django import forms
from .models import *

class CustomMemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['photo', 'name', 'category', 'bag', 'institution', 'email', 'fone', 'git', 'lattes', 'link', 'insta', 'twt', 'face', 'youtube', 'cpf', 'rg', 'gender', 'formation', 'birthday', 'address', 'project', 'award', 'bankName', 'bankNumber', 'agencyNumber', 'accountNumber', 'commitment', 'science', 'jobPlan', 'lgpd']
        widgets = {
            "birthday": forms.TextInput(attrs={'class':'form-control', 'type':'date'})
        }

class CustomHubForm(forms.ModelForm):
    class Meta:
        model = Hub
        fields = ['photo', 'name', 'headquarter', 'region', 'representative', 'institutions', 'participants', 'connection', 'amountStudents', 'description']

class CustomInstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = ['photo', 'name', 'email', 'fone', 'site', 'hub', 'sphere', 'address', 'amountStudents', 'description']

class CustomProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['photo', 'name', 'institution', 'ptype', 'financier', 'description', 'relatory']

