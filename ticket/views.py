from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'ticket/home.html'
    extra_context = {'today': datetime.today()}
    login_url = '/login'


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = '/issue_tickets'


class LoginUserView(LoginView):
    template_name = 'login.html'
    success_url = ''
