# Generated by Django 4.0.2 on 2022-03-08 17:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_user__url_user_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date_started',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
