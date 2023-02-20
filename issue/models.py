from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class Project(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    title = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.id

    def __str__(self):
        return str(self.id)


class Issue(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    title = models.CharField(max_length=300)
    problem_description = models.CharField(max_length=7000, null=True, blank=True, default=None)
    raised_on = models.DateTimeField(auto_now_add=True)
    opened_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='opened_issues')
    closed_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='closed_issues', null=True, default=None,
                                  blank=True)
    closed_on = models.DateTimeField(null=True, default="", blank=True)
    project = models.ForeignKey(Project, on_delete=models.SET_DEFAULT, default=0)
