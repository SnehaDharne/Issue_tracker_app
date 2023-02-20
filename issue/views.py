from django.shortcuts import render
from django.http import Http404
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.datetime_safe import datetime
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.views.generic.edit import DeleteView
from .models import Project, Issue, User
from .forms import IssueForm


class DeleteIssueView(DeleteView):
    model = Issue
    success_url = '/issue_tickets'
    template_name = 'issue/issue_delete.html'


class UpdateIssueView(UpdateView):
    model = Issue
    fields = ['closed_on', 'closed_by']  # include the fields you want to update here
    success_url = '/issue_tickets/'  # replace with your own success URL

    def form_valid(self, form):
        issue = form.save(commit=False)
        # update the closed_by field with a specific user
        user = User.objects.get(username='user1')
        issue.closed_by = user
        issue.closed_on = timezone.datetime.now()
        issue.save()
        return super().form_valid(form)


class CreateIssueView(CreateView):
    model = Issue
    form_class = IssueForm
    success_url = '/issue_tickets'

    def form_valid(self, form):
        # Set the value of closed_on to None before saving the form
        form.instance.closed_on = None
        return super().form_valid(form)


class IssueListView(ListView):
    model = Issue
    context_object_name = "issue"
    template_name = "issue/issue_list.html"


# def list_issue(request):
#     all_issues = Issue.objects.all()
#     return render(request, 'issue/issue_list.html', {'issue': all_issues})

class IssueDetailView(DetailView):
    model = Issue
    context_object_name = "ticket"
    template_name = "issue/issue_detail.html"


# def detail(request, pk):
#     try:
#         ticket = Issue.objects.get(pk=pk)
#     except Issue.DoesNotExist:
#         raise Http404("Issue does not exist")
#     return render(request, 'issue/issue_list.html', {'ticket': ticket})

class ProjectDetailView(DetailView):
    model = Project
    context_object_name = "project"
    template_name = "issue/issue_detail.html"


class UserDetailView(DetailView):
    model = User
    context_object_name = "user"
    template_name = "issue/issue_detail.html"
