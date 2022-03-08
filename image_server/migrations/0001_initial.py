# Generated by Django 4.0.2 on 2022-03-08 21:37

from django.db import migrations, models
import pathlib


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('uid', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('image', models.ImageField(max_length=255, upload_to=pathlib.PurePosixPath('image_server/storage'))),
            ],
        ),
    ]
