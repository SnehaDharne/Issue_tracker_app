# Generated by Django 4.1.5 on 2023-02-17 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0019_alter_issue_problem_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='project_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='issue.project'),
        ),
        migrations.AlterField(
            model_name='user',
            name='project_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='issue.project'),
        ),
    ]