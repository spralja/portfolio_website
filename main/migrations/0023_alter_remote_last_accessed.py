# Generated by Django 4.0.2 on 2022-02-26 07:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_alter_remote_last_accessed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remote',
            name='last_accessed',
            field=models.DateTimeField(default=datetime.datetime(1970, 1, 1, 1, 0)),
        ),
    ]
