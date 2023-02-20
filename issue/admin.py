from django.contrib import admin

# Register your models here.
from . import models


class IssuesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'raised_on', 'opened_by', 'closed_on', 'closed_by', 'project']


# class UserAdmin(admin.ModelAdmin):
#     list_display = ['username', 'project_id']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'id']


admin.site.register(models.Issue, IssuesAdmin)
# admin.site.register(models.User, UserAdmin)
admin.site.register(models.Project, ProjectAdmin)
