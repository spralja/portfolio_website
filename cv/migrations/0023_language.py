# Generated by Django 3.2.7 on 2021-10-02 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0022_technicalskill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('level', models.CharField(max_length=20)),
            ],
        ),
    ]