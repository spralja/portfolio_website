# Generated by Django 3.2.7 on 2021-10-02 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0019_course_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
