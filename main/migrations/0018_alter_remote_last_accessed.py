# Generated by Django 4.0.2 on 2022-02-26 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_remote_last_accessed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remote',
            name='last_accessed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
