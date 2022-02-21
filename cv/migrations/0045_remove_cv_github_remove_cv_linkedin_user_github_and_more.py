# Generated by Django 4.0.2 on 2022-02-20 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0044_remove_cv_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cv',
            name='github',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='linkedin',
        ),
        migrations.AddField(
            model_name='user',
            name='github',
            field=models.URLField(default='www.google.com'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='linkedin',
            field=models.URLField(default='www.google.com'),
            preserve_default=False,
        ),
    ]
