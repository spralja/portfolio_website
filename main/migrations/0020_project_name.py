# Generated by Django 4.0.2 on 2022-02-26 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_remove_staticwebsite_github_repository_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
