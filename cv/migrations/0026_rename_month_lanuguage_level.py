# Generated by Django 3.2.7 on 2021-10-02 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0025_rename_date2_lanuguage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lanuguage',
            old_name='month',
            new_name='level',
        ),
    ]
