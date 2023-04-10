from django import forms
from .models import *

class CustomMemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['photo', 'name', 'category', 'institution', 'email', 'fone', 'git', 'lattes', 'link', 'insta', 'twt', 'face', 'youtube', 'cpf', 'rg', 'gender', 'formation', 'birthday', 'address', 'project', 'bankName', 'bankNumber', 'agencyNumber', 'accountNumber', 'commitment', 'science', 'jobPlan', 'lgpd']
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

class CustomScholarshipForm(forms.ModelForm):
    class Meta:
        model = Scholarship
        fields = ['member','stype', 'value', 'financier', 'dateStart', 'dateEnd', 'description', 'relatory']
        widgets = {
            "dateStart": forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
            "dateEnd": forms.TextInput(attrs={'class':'form-control', 'type':'date'})
        }

class CustomPublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['member', 'title', 'publicationType', 'event', 'linkEvent', 'description', 'pdf']

class CustomEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'eventType', 'dateStart', 'dateEnd', 'organization', 'address', 'description']
        widgets = {
            "dateStart": forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
            "dateEnd": forms.TextInput(attrs={'class':'form-control', 'type':'date'})
        }

class CustomCertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['name', 'project', 'event', 'cpf', 'hours', 'description', 'code', 'pdf']

class CustomAwardForm(forms.ModelForm):
    class Meta:
        model = Award
        fields = ['title', 'member', 'atype', 'organization', 'description', 'pdf']

class CustomStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'gender', 'birthday', 'school', 'mannaNumber', 'hub', 'project', 'event']
        widgets = {
            "birthday": forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
        }