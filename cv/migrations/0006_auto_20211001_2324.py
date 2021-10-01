# Generated by Django 3.2.7 on 2021-10-01 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0005_auto_20211001_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='end_month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='experience',
            name='end_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='experience',
            name='start_month',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='experience',
            name='start_year',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]