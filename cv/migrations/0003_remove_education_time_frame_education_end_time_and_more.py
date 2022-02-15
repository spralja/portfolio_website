# Generated by Django 4.0.2 on 2022-02-15 12:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_alter_cv_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='time_frame',
        ),
        migrations.AddField(
            model_name='education',
            name='end_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 15, 13, 1, 13, 176225)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cv',
            name='name',
            field=models.CharField(default='main', max_length=200, primary_key=True, serialize=False),
        ),
    ]
