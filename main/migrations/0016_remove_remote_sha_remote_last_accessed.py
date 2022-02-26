# Generated by Django 4.0.2 on 2022-02-26 07:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_remote_sha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='remote',
            name='sha',
        ),
        migrations.AddField(
            model_name='remote',
            name='last_accessed',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 26, 8, 23, 25, 716534)),
            preserve_default=False,
        ),
    ]