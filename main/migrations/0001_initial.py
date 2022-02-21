# Generated by Django 4.0.2 on 2022-02-21 14:54

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('github', models.URLField()),
                ('linkedin', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='TechnicalSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='technical_skills', to='main.user')),
            ],
            options={
                'unique_together': {('parent', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('heading', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resumes', to='main.user')),
            ],
            options={
                'verbose_name': 'Résumé',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='main.education')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('alt', models.CharField(max_length=255)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='main.user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraph', models.TextField()),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paragraphs', to='main.resume')),
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
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='languages', to='main.user')),
            ],
            options={
                'unique_together': {('parent', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hobbies', to='main.user')),
            ],
            options={
                'verbose_name_plural': 'Hobbies',
                'unique_together': {('parent', 'name')},
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
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to='main.user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='education',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='main.user'),
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('description', models.TextField(primary_key=True, serialize=False)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='descriptions', to='main.experience')),
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
                ('user_picture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.picture')),
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
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='main.education')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
