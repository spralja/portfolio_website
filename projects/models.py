from django.db import models

DEFAULT_MAX_LENGTH = 255


class Project(models.Model):
    name = models.CharField(max_length=DEFAULT_MAX_LENGTH, primary_key=True)

class Image(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    name = models.CharField(max_length=DEFAULT_MAX_LENGTH, primary_key=True)
    image = models.ImageField(upload_to='projects/images/')
