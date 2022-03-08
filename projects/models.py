from django.db import models

DEFAULT_MAX_LENGTH = 255


class Image(models.Model):
    name = models.CharField(max_length=DEFAULT_MAX_LENGTH, primary_key=True)
    image = models.ImageField(upload_to='projects/images/')
