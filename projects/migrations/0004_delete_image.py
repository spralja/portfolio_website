# Generated by Django 4.0.2 on 2022-03-08 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_remove_image_project_delete_project'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
    ]
