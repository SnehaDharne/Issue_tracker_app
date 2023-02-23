from django import forms

from project_management.models import Project
from .models import Issue


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['title', 'problem_description', 'project','attachment']
        attachment = forms.FileField(required=False)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'problem_description': forms.Textarea(attrs={'class': 'form-control mb-5'}),
        }
        labels = {
            'title': 'Enter the Ticket Title',
            'problem_description': 'Description of the issue ',

        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields['project'].queryset = Project.objects.filter(users=user)
