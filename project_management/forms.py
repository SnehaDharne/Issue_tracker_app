from django import forms
from .models import Project
from django.contrib.auth import get_user_model


class ProjectCreateForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Project
        fields = ['name', 'description', 'users']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.fields['users'].queryset.exists():
            self.fields['users'].initial = [self.fields['users'].queryset.first().pk]