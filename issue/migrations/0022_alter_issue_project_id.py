# Generated by Django 4.1.5 on 2023-02-17 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0021_alter_issue_project_id_alter_user_project_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='project_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='issue.project'),
        ),
    ]
