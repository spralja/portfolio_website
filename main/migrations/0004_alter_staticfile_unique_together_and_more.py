# Generated by Django 4.0.2 on 2022-02-26 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_project_remote_remote_project_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='staticfile',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='staticfile',
            name='static_website',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='static_files', to='main.staticwebsite'),
        ),
        migrations.AlterUniqueTogether(
            name='staticfile',
            unique_together={('static_website', 'name')},
        ),
        migrations.RemoveField(
            model_name='staticfile',
            name='project',
        ),
    ]