# Generated by Django 3.2.7 on 2021-10-01 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0003_alter_experience_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='hide',
            field=models.BooleanField(default=False),
        ),
    ]