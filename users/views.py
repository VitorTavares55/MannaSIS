from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView

from .models import Status

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			Status.objects.create(user=user)
			return redirect("login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="users/register.html", context={"register_form":form})

class StatusList(LoginRequiredMixin, UserPassesTestMixin, ListView):
	def test_func(self):
		return is_director(self.request.user) and is_auth(self.request.user)
	model = Status
	template_name = 'users/user-list.html'

class StatusUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	def test_func(self):
		return is_director(self.request.user) and is_auth(self.request.user)
	model = Status
	template_name = 'users/user-form.html'
	fields = ['auth', 'division']
	success_url = reverse_lazy('user-list')

def is_auth(user):
	return user.status.auth == True

def is_header(user):
    return user.status.division == 'Lider'

def is_director(user):
    return user.status.division == 'Diretoria'