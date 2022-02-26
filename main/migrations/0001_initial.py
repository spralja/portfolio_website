# Generated by Django 4.0.2 on 2022-02-26 09:50

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import main.models
import portfolio_website.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('alt', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('title', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False, validators=[main.models.NotTakenNameValidator])),
                ('_description', portfolio_website.models.MarkdownField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Remote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation', models.CharField(max_length=255)),
                ('repository', models.CharField(max_length=255)),
                ('branch', models.CharField(default='main', max_length=255)),
                ('last_accessed', models.DateTimeField(default=datetime.datetime(1970, 1, 1, 1, 0))),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.project')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('about_me', models.TextField(blank=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('github', models.URLField(null=True)),
                ('gitlab', models.URLField(null=True)),
                ('linkedin', models.URLField(null=True)),
                ('picture', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.picture')),
            ],
        ),
        migrations.CreateModel(
            name='TechnicalSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='technical_skills', to='main.user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('heading', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resumes', to='main.user')),
            ],
            options={
                'verbose_name': 'Résumé',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='main.user'),
        ),
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraph', models.TextField()),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paragraphs', to='main.resume')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(choices=[(1, 'elementary'), (2, 'professional'), (3, 'fluent')])),
                ('name', models.CharField(max_length=255)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='languages', to='main.user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hobbies', to='main.user')),
            ],
            options={
                'verbose_name_plural': 'Hobbies',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authority', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('start_time', models.DateField()),
                ('end_time', models.DateField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to='main.user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authority', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('major', models.CharField(max_length=255)),
                ('gpa', models.FloatField(validators=[django.core.validators.MinValueValidator(-3.0), django.core.validators.MaxValueValidator(12.0)])),
                ('start_time', models.DateField()),
                ('end_time', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='main.user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('description', models.TextField(primary_key=True, serialize=False)),
                ('experience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='descriptions', to='main.experience')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CV',
            fields=[
                ('name', models.CharField(default='main', max_length=255, primary_key=True, serialize=False)),
                ('educations', models.ManyToManyField(blank=True, to='main.Education')),
                ('experiences', models.ManyToManyField(blank=True, to='main.Experience')),
                ('hobbies', models.ManyToManyField(blank=True, to='main.Hobby')),
                ('languages', models.ManyToManyField(blank=True, to='main.Language')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.resume')),
                ('technical_skills', models.ManyToManyField(blank=True, to='main.TechnicalSkill')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cvs', to='main.user')),
            ],
            options={
                'verbose_name': 'Curriculum Vitae',
                'verbose_name_plural': 'Curricula Vitae',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='main.education')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StaticFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('remote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='static_files', to='main.remote')),
            ],
            options={
                'unique_together': {('remote', 'name')},
            },
        ),
    ]