# Generated by Django 3.2.7 on 2021-10-01 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0011_auto_20211002_0146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='end_date',
        ),
    ]
