# Generated by Django 4.1.5 on 2023-02-16 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0017_alter_issue_closed_by_alter_issue_closed_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='closed_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='closed_issues', to='issue.user'),
        ),
    ]