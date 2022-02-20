# Generated by Django 4.0.2 on 2022-02-20 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0038_alter_resume_options_education_major'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cv',
            name='name',
            field=models.CharField(default='main', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cv',
            name='user_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='description',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='education',
            name='authority',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='education',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='experience',
            name='authority',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='experience',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='resume',
            name='heading',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='technicalskill',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='userpicture',
            name='alt',
            field=models.CharField(max_length=255),
        ),
    ]
