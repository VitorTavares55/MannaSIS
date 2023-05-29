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

class IndexView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = "pages/index.html"

class MemberList(LoginRequiredMixin, ListView):
	login_url = reverse_lazy('login')
	model = Member
	template_name = 'pages/member-list.html'

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
        result = Member.objects.filter(id__iexact=value)
        scholarship = Scholarship.objects.filter(member__id__iexact=value)
        return render(request, 'pages/member-profile.html', dict(result=result, scholarship=scholarship))

class MemberCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = CustomMemberForm
    template_name = 'pages/form.html'
    model = Member
    success_url = reverse_lazy('membros')

class MemberUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    form_class = CustomMemberForm
    template_name = 'pages/form.html'
    model = Member
    success_url = reverse_lazy('membros')

class MemberDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    template_name = 'pages/delete.html'
    model = Member
    success_url = reverse_lazy('membros')

#-------------------------------------------------------------------------#

class HubList(LoginRequiredMixin, ListView):
	login_url = reverse_lazy('login')
	model = Hub
	template_name = 'pages/hub-list.html'

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
        result = Hub.objects.filter(id__iexact=value)
        institutions = Institution.objects.filter(hub__id__iexact=value)
        return render(request, 'pages/hub-profile.html', dict(result=result, institutions=institutions))

class HubCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = CustomHubForm
    template_name = 'pages/form.html'
    model = Hub
    success_url = reverse_lazy('hubs')

class HubUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    form_class = CustomHubForm
    template_name = 'pages/form.html'
    model = Hub
    success_url = reverse_lazy('hubs')

class HubDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    template_name = 'pages/delete.html'
    model = Hub
    success_url = reverse_lazy('hubs')

#-------------------------------------------------------------------------#

class InstitutionList(ListView):
	login_url = reverse_lazy('login')
	model = Institution
	template_name = 'pages/institution-list.html'

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
        result = Institution.objects.filter(name__iexact=value)
        return render(request, 'pages/institution-profile.html', {'result':result})

class InstitutionCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = CustomInstitutionForm
    template_name = 'pages/form.html'
    model = Institution
    success_url = reverse_lazy('instituicoes')

class InstitutionUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    form_class = CustomInstitutionForm
    template_name = 'pages/form.html'
    model = Institution
    success_url = reverse_lazy('instituicoes')

class InstitutionDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    template_name = 'pages/delete.html'
    model = Institution
    success_url = reverse_lazy('instituicoes')

#-------------------------------------------------------------------------#

class ProjectList(LoginRequiredMixin, ListView):
	login_url = reverse_lazy('login')
	model = Project
	template_name = 'pages/project-list.html'

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
        result = Project.objects.filter(id__iexact=value)
        members = Member.objects.filter(project__id__iexact=value)
        return render(request, 'pages/project-profile.html', dict(result = result, members = members))
  

class ProjectCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = CustomProjectForm
    template_name = 'pages/form.html'
    model = Project
    success_url = reverse_lazy('projetos')

class ProjectUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    form_class = CustomProjectForm
    template_name = 'pages/form.html'
    model = Project
    success_url = reverse_lazy('projetos')

class ProjectDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    template_name = 'pages/delete.html'
    model = Project
    success_url = reverse_lazy('projetos')

#-------------------------------------------------------------------------#

class ScholarshipList(LoginRequiredMixin, ListView):
	login_url = reverse_lazy('login')
	model = Scholarship
	template_name = 'pages/scholarship-list.html'

def scholarshipfilter(request):
    if request.method == 'POST':
        value = request.POST['search']
        result = Scholarship.objects.filter(member__contains=value)
        return render(request, 'pages/scholarship-filter.html', {'result':result})
    else:
        return render(request, 'pages/scholarship-list.html', {})

def scholarshipprofile(request):
  if request.method == 'POST':
        value = request.POST['value']
        result = Scholarship.objects.filter(id__iexact=value)
        return render(request, 'pages/scholarship-profile.html', dict(result = result))
  

class ScholarshipCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = CustomScholarshipForm
    template_name = 'pages/form.html'
    model = Scholarship
    success_url = reverse_lazy('bolsas')

class ScholarshipUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    form_class = CustomScholarshipForm
    template_name = 'pages/form.html'
    model = Scholarship
    success_url = reverse_lazy('bolsas')

class ScholarshipDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    template_name = 'pages/delete.html'
    model = Scholarship
    success_url = reverse_lazy('bolsas')

#-------------------------------------------------------------------------#

class PublicationList(LoginRequiredMixin, ListView):
	login_url = reverse_lazy('login')
	model = Publication
	template_name = 'pages/publication-list.html'

def publicationfilter(request):
    if request.method == 'POST':
        value = request.POST['search']
        result = Publication.objects.filter(title__contains=value)
        return render(request, 'pages/publication-filter.html', {'result':result})
    else:
        return render(request, 'pages/publication-list.html', {})

def publicationprofile(request):
  if request.method == 'POST':
        value = request.POST['value']
        result = Publication.objects.filter(id__iexact=value)
        members = Member.objects.filter(publication__id__iexact=value)
        return render(request, 'pages/publication-profile.html', dict(result = result, members = members))
  

class PublicationCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = CustomPublicationForm
    template_name = 'pages/form.html'
    model = Publication
    success_url = reverse_lazy('publicacoes')

class PublicationUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    form_class = CustomPublicationForm
    template_name = 'pages/form.html'
    model = Publication
    success_url = reverse_lazy('publicacoes')

class PublicationDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    template_name = 'pages/delete.html'
    model = Publication
    success_url = reverse_lazy('publicacoes')

#-------------------------------------------------------------------------#

class EventList(LoginRequiredMixin, ListView):
	login_url = reverse_lazy('login')
	model = Event
	template_name = 'pages/event-list.html'

def eventfilter(request):
    if request.method == 'POST':
        value = request.POST['search']
        result = Event.objects.filter(title__contains=value)
        return render(request, 'pages/event-filter.html', {'result':result})
    else:
        return render(request, 'pages/event-list.html', {})

def eventprofile(request):
  if request.method == 'POST':
        value = request.POST['value']
        result = Event.objects.filter(id__iexact=value)
        members = Member.objects.filter(event__id__iexact=value)
        return render(request, 'pages/event-profile.html', dict(result = result, members = members))
  

class EventCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = CustomEventForm
    template_name = 'pages/form.html'
    model = Event
    success_url = reverse_lazy('eventos')

class EventUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    form_class = CustomEventForm
    template_name = 'pages/form.html'
    model = Event
    success_url = reverse_lazy('eventos')

class EventDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    template_name = 'pages/delete.html'
    model = Event
    success_url = reverse_lazy('eventos')

#-------------------------------------------------------------------------#

class CertificateList(LoginRequiredMixin, ListView):
	login_url = reverse_lazy('login')
	model = Certificate
	template_name = 'pages/certificate-list.html'

def certificatefilter(request):
    if request.method == 'POST':
        value = request.POST['search']
        result = Certificate.objects.filter(member__contains=value)
        return render(request, 'pages/certificate-filter.html', {'result':result})
    else:
        return render(request, 'pages/certificate-list.html', {})

def certificateprofile(request):
  if request.method == 'POST':
        value = request.POST['value']
        result = Certificate.objects.filter(id__iexact=value)
        return render(request, 'pages/certificate-profile.html', dict(result = result))
  

class CertificateCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = CustomCertificateForm
    template_name = 'pages/form.html'
    model = Certificate
    success_url = reverse_lazy('certificados')

class CertificateUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    form_class = CustomCertificateForm
    template_name = 'pages/form.html'
    model = Certificate
    success_url = reverse_lazy('certificados')

class CertificateDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    template_name = 'pages/delete.html'
    model = Certificate
    success_url = reverse_lazy('certificados')

#-------------------------------------------------------------------------#

class AwardList(LoginRequiredMixin, ListView):
	login_url = reverse_lazy('login')
	model = Award
	template_name = 'pages/award-list.html'

def awardfilter(request):
    if request.method == 'POST':
        value = request.POST['search']
        result = Award.objects.filter(member__contains=value)
        return render(request, 'pages/award-filter.html', {'result':result})
    else:
        return render(request, 'pages/award-list.html', {})

def awardprofile(request):
  if request.method == 'POST':
        value = request.POST['value']
        result = Award.objects.filter(id__iexact=value)
        return render(request, 'pages/award-profile.html', dict(result = result))
  

class AwardCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = CustomAwardForm
    template_name = 'pages/form.html'
    model = Award
    success_url = reverse_lazy('premios')

class AwardUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    form_class = CustomAwardForm
    template_name = 'pages/form.html'
    model = Award
    success_url = reverse_lazy('premios')

class AwardDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    template_name = 'pages/delete.html'
    model = Award
    success_url = reverse_lazy('premios')

#-------------------------------------------------------------------------#

class StudentList(LoginRequiredMixin, ListView):
	login_url = reverse_lazy('login')
	model = Student
	template_name = 'pages/student-list.html'

def studentfilter(request):
    if request.method == 'POST':
        value = request.POST['search']
        result = Student.objects.filter(member__contains=value)
        return render(request, 'pages/student-filter.html', {'result':result})
    else:
        return render(request, 'pages/student-list.html', {})

def studentprofile(request):
  if request.method == 'POST':
        value = request.POST['value']
        result = Student.objects.filter(id__iexact=value)
        return render(request, 'pages/student-profile.html', dict(result = result))
  

class StudentCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = CustomStudentForm
    template_name = 'pages/form.html'
    model = Student
    success_url = reverse_lazy('alunos')

class StudentUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    form_class = CustomStudentForm
    template_name = 'pages/form.html'
    model = Student
    success_url = reverse_lazy('alunos')

class StudentDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    template_name = 'pages/delete.html'
    model = Student
    success_url = reverse_lazy('alunos')