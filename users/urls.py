from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path("registrar", views.register_request, name="register"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('users/', StatusList.as_view(), name='user-list'),
    path('users/<int:pk>/update/', StatusUpdate.as_view(), name='user-update'),
]