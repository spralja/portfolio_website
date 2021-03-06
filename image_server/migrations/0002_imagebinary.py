# Generated by Django 4.0.2 on 2022-03-09 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('image_server', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageBinary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('binary', models.BinaryField()),
                ('content_type', models.CharField(max_length=255)),
                ('image', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='image_binary', to='image_server.image')),
            ],
        ),
    ]
