from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms
from django.shortcuts import get_object_or_404, render
from .models import *
from .forms import *

# Create your views here.

class IndexView(TemplateView):
    template_name = "pages/index.html"

class LoginView(TemplateView):
    template_name = "pages/login.html"

##class MemberList(LoginRequiredMixin, ListView):
class MemberList(ListView):
	#login_url = reverse_lazy('login')
	model = Member
	template_name = 'pages/member-list.html'
	#success_url = reverse_lazy('index')

def memberfilter(request):
    if request.method == 'POST':
        value = request.POST['search']
        result = Member.objects.filter(name__contains=value)
        return render(request, 'pages/member-filter.html', {'result':result})
    else:
        return render(request, 'pages/member-list.html', {})

def memberprofile(request):
  if request.method == 'POST':
        value = request.POST['value']
        result = Member.objects.filter(name__contains=value)
        return render(request, 'pages/member-profile.html', {'result':result})

class MemberCreate(CreateView):
    form_class = CustomMemberForm
    template_name = 'pages/form.html'
    model = Member
    success_url = reverse_lazy('membros')

class MemberUpdate(UpdateView):
    form_class = CustomMemberForm
    template_name = 'pages/form.html'
    model = Member
    success_url = reverse_lazy('membros')

class MemberDelete(DeleteView):
    template_name = 'pages/delete.html'
    model = Member
    success_url = reverse_lazy('membros')


class HubList(ListView):
	#login_url = reverse_lazy('login')
	model = Hub
	template_name = 'pages/hub-list.html'
	#success_url = reverse_lazy('index')

def hubfilter(request):
    if request.method == 'POST':
        value = request.POST['search']
        result = Hub.objects.filter(name__contains=value)
        return render(request, 'pages/hub-filter.html', {'result':result})
    else:
        return render(request, 'pages/hub-list.html', {})

def hubprofile(request):
  if request.method == 'POST':
        value = request.POST['value']
        result = Hub.objects.filter(name__contains=value)
        return render(request, 'pages/hub-profile.html', {'result':result})

class HubCreate(CreateView):
    form_class = CustomHubForm
    template_name = 'pages/form.html'
    model = Hub
    success_url = reverse_lazy('hubs')

class HubUpdate(UpdateView):
    form_class = CustomHubForm
    template_name = 'pages/form.html'
    model = Hub
    success_url = reverse_lazy('hubs')

class HubDelete(DeleteView):
    template_name = 'pages/delete.html'
    model = Hub
    success_url = reverse_lazy('hubs')



class InstitutionList(ListView):
	#login_url = reverse_lazy('login')
	model = Institution
	template_name = 'pages/institution-list.html'
	#success_url = reverse_lazy('index')

def institutionfilter(request):
    if request.method == 'POST':
        value = request.POST['search']
        result = Institution.objects.filter(name__contains=value)
        return render(request, 'pages/institution-filter.html', {'result':result})
    else:
        return render(request, 'pages/institution-list.html', {})

def institutionprofile(request):
  if request.method == 'POST':
        value = request.POST['value']
        result = Institution.objects.filter(name__contains=value)
        return render(request, 'pages/institution-profile.html', {'result':result})

class InstitutionCreate(CreateView):
    form_class = CustomInstitutionForm
    template_name = 'pages/form.html'
    model = Institution
    success_url = reverse_lazy('instituicoes')

class InstitutionUpdate(UpdateView):
    form_class = CustomInstitutionForm
    template_name = 'pages/form.html'
    model = Institution
    success_url = reverse_lazy('instituicoes')

class InstitutionDelete(DeleteView):
    template_name = 'pages/delete.html'
    model = Institution
    success_url = reverse_lazy('instituicoes')



class ProjectList(ListView):
	#login_url = reverse_lazy('login')
	model = Project
	template_name = 'pages/project-list.html'
	#success_url = reverse_lazy('index')

def projectfilter(request):
    if request.method == 'POST':
        value = request.POST['search']
        result = Project.objects.filter(name__contains=value)
        return render(request, 'pages/project-filter.html', {'result':result})
    else:
        return render(request, 'pages/project-list.html', {})

def projectprofile(request):
  if request.method == 'POST':
        value = request.POST['value']
        result = Project.objects.filter(name__contains=value)
        return render(request, 'pages/project-profile.html', {'result':result})

class ProjectCreate(CreateView):
    form_class = CustomProjectForm
    template_name = 'pages/form.html'
    model = Project
    success_url = reverse_lazy('projetos')

class ProjectUpdate(UpdateView):
    form_class = CustomProjectForm
    template_name = 'pages/form.html'
    model = Project
    success_url = reverse_lazy('projetos')

class ProjectDelete(DeleteView):
    template_name = 'pages/delete.html'
    model = Project
    success_url = reverse_lazy('projetos')

