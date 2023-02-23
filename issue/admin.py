from django.contrib import admin

# Register your models here.
from . import models


class IssuesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'raised_on', 'opened_by', 'closed_on', 'closed_by', 'project']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'description']


admin.site.register(models.Issue, IssuesAdmin)
admin.site.register(models.Project, ProjectAdmin)
