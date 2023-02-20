from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'ticket/home.html'
    extra_context = {'today': datetime.today()}


class AuthorizedView(LoginRequiredMixin,TemplateView):
    template_name = 'ticket/authorized.html'
    login_url = '/admin'

