from django import forms
from .models import Issue


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ('title', 'problem_description', 'opened_by', 'project')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'problem_description': forms.Textarea(attrs={'class': 'form-control mb-5'}),
        }
        labels = {
            'title': 'Enter the Ticket Title',
            'problem_description': 'Description of the issue ',

        }
