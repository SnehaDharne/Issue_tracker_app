# Generated by Django 4.1.5 on 2023-01-27 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0013_remove_user_username_alter_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='id',
            new_name='username',
        ),
    ]
