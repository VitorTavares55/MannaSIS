from django.http import HttpRequest
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('login', LoginView.as_view(), name="login"),
    path('membros', MemberList.as_view(), name="membros"),
    path('cadastro-membro', MemberCreate.as_view(), name="cadastro-membro"),
    path('editar-membro/<int:pk>/', MemberUpdate.as_view(), name="editar-membro"),
    path('deletar-membro/<int:pk>/', MemberDelete.as_view(), name="deletar-membro"),
    path('filtro-membro', views.memberfilter, name="filtro-membro"),
    path('membro', views.memberprofile, name="membro"),

    path('instituicoes', InstitutionList.as_view(), name="instituicoes"),
    path('cadastro-instituicao', InstitutionCreate.as_view(), name="cadastro-instituicao"),
    path('editar-instituicao/<int:pk>/', InstitutionUpdate.as_view(), name="editar-instituicao"),
    path('deletar-instituicao/<int:pk>/', InstitutionDelete.as_view(), name="deletar-instituicao"),
    path('filtro-instituicao', views.institutionfilter, name="filtro-instituicao"),
    path('instituicao', views.institutionprofile, name="instituicao"),
]
