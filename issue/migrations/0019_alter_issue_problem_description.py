# Generated by Django 4.1.5 on 2023-02-16 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0018_alter_issue_closed_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='problem_description',
            field=models.CharField(blank=True, default=None, max_length=7000, null=True),
        ),
    ]