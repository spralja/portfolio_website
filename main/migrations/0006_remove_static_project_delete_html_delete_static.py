# Generated by Django 4.0.2 on 2022-02-26 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_staticwebsite_remote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='static',
            name='project',
        ),
        migrations.DeleteModel(
            name='Html',
        ),
        migrations.DeleteModel(
            name='Static',
        ),
    ]