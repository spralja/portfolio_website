# Generated by Django 4.0.2 on 2022-02-15 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0035_rename_name_project_title'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='project',
            unique_together={('parent', 'title')},
        ),
        migrations.RemoveField(
            model_name='project',
            name='description',
        ),
    ]
