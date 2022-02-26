# Generated by Django 4.0.2 on 2022-02-26 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_rename_git_object_remote_branch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='remote',
            name='last_accessed',
        ),
        migrations.AddField(
            model_name='remote',
            name='sha',
            field=models.CharField(max_length=255, null=True),
        ),
    ]