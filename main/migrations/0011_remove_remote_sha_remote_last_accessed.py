# Generated by Django 4.0.2 on 2022-02-26 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_rename_hash_remote_sha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='remote',
            name='sha',
        ),
        migrations.AddField(
            model_name='remote',
            name='last_accessed',
            field=models.DateTimeField(null=True),
        ),
    ]