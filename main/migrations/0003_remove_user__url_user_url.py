# Generated by Django 4.0.2 on 2022-03-06 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_user__url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='_url',
        ),
        migrations.AddField(
            model_name='user',
            name='url',
            field=models.URLField(default='www.github.com'),
            preserve_default=False,
        ),
    ]
