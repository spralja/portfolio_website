# Generated by Django 4.0.2 on 2022-02-15 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0024_cv_github'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='linkedin',
            field=models.URLField(default='https://www.linkedin.com/in/rspralja/'),
            preserve_default=False,
        ),
    ]
