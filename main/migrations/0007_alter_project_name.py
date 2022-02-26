# Generated by Django 4.0.2 on 2022-02-26 05:59

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_static_project_delete_html_delete_static'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=255, primary_key=True, serialize=False, validators=[main.models.NotTakenNameValidator]),
        ),
    ]
