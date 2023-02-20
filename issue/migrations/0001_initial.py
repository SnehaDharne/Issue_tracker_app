# Generated by Django 4.1.5 on 2023-01-26 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=300)),
                ('raised_on', models.DateTimeField(auto_now_add=True)),
                ('closed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='closed_issues', to='issue.user')),
                ('opened_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opened_issues', to='issue.user')),
            ],
        ),
    ]
