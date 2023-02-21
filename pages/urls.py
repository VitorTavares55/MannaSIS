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

    path('hubs', HubList.as_view(), name="hubs"),
    path('cadastro-hub', HubCreate.as_view(), name="cadastro-hub"),
    path('editar-hub/<int:pk>/', HubUpdate.as_view(), name="editar-hub"),
    path('deletar-hub/<int:pk>/', HubDelete.as_view(), name="deletar-hub"),
    path('filtro-hub', views.hubfilter, name="filtro-hub"),
    path('hub', views.hubprofile, name="hub"),

    path('instituicoes', InstitutionList.as_view(), name="instituicoes"),
    path('cadastro-instituicao', InstitutionCreate.as_view(), name="cadastro-instituicao"),
    path('editar-instituicao/<int:pk>/', InstitutionUpdate.as_view(), name="editar-instituicao"),
    path('deletar-instituicao/<int:pk>/', InstitutionDelete.as_view(), name="deletar-instituicao"),
    path('filtro-instituicao', views.institutionfilter, name="filtro-instituicao"),
    path('instituicao', views.institutionprofile, name="instituicao"),

    path('projetos', ProjectList.as_view(), name="projetos"),
    path('cadastro-projeto', ProjectCreate.as_view(), name="cadastro-projeto"),
    path('editar-projeto/<int:pk>/', ProjectUpdate.as_view(), name="editar-projeto"),
    path('deletar-projeto/<int:pk>/', ProjectDelete.as_view(), name="deletar-projeto"),
    path('filtro-projeto', views.projectfilter, name="filtro-projeto"),
    path('projeto', views.projectprofile, name="projeto"),

    path('bolsas', ScholarshipList.as_view(), name="bolsas"),
    path('cadastro-bolsa', ScholarshipCreate.as_view(), name="cadastro-bolsa"),
    path('editar-bolsa/<int:pk>/', ScholarshipUpdate.as_view(), name="editar-bolsa"),
    path('deletar-bolsa/<int:pk>/', ScholarshipDelete.as_view(), name="deletar-bolsa"),
    path('filtro-bolsa', views.scholarshipfilter, name="filtro-bolsa"),
    path('bolsa', views.scholarshipprofile, name="bolsa"),
]
