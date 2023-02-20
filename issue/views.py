from django.shortcuts import render
from django.http import Http404
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.datetime_safe import datetime
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView
from .models import Project, Issue
from django.contrib.auth import get_user_model
from .forms import IssueForm


class DeleteIssueView(DeleteView):
    model = Issue
    success_url = '/issue_tickets'
    template_name = 'issue/issue_delete.html'


class UpdateIssueView(LoginRequiredMixin, UpdateView):
    model = Issue
    fields = ['closed_on', 'closed_by']  # include the fields you want to update here
    success_url = '/issue_tickets/'  # replace with your own success URL
    login_url = '/login'

    def form_valid(self, form):
        issue = form.save(commit=False)
        # update the closed_by field with a specific user
        user = self.request.user
        issue.closed_by = user
        issue.closed_on = timezone.datetime.now()
        issue.save()
        return super().form_valid(form)


class CreateIssueView(LoginRequiredMixin, CreateView):
    model = Issue
    form_class = IssueForm
    success_url = '/issue_tickets'
    login_url = '/login'

    def form_valid(self, form):
        # Set the value of closed_on to None before saving the form
        form.instance.closed_on = None
        issue = form.save(commit=False)
        user = self.request.user
        issue.opened_by = user
        return super().form_valid(form)


class IssueListView(LoginRequiredMixin, ListView):
    model = Issue
    context_object_name = "issue"
    template_name = "issue/issue_list.html"
    login_url = '/login'


class IssueDetailView(DetailView):
    model = Issue
    context_object_name = "ticket"
    template_name = "issue/issue_detail.html"


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = "project"
    template_name = "issue/issue_detail.html"
