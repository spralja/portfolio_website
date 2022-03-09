from portfolio_website.settings import BASE_DIR, DEFAULT_MAX_LENGTH

from django.db import models

from pathlib import Path


class Image(models.Model):
    uid = models.CharField(max_length=DEFAULT_MAX_LENGTH, primary_key=True)
    image = models.ImageField(upload_to=Path('image_server') / 'storage', max_length=DEFAULT_MAX_LENGTH)

    @property
    def path(self):
        return Path(self.image.name)

    def get_raw(self):
        with open(self.path, 'rb') as file:
            return file.read()

    def get_content_type(self):
        content_type = 'image/'
        file_extension = str(self.path).split('.')[-1]
        if file_extension in {'jpg', 'jpeg'}:
            content_type += 'jpeg'
        elif file_extension == 'png':
            content_type += 'png'
        else:
            content_type += 'unknown'

        return content_type

    def __str__(self):
        return self.uid

class ImageBinary(models.Model):
    image = models.OneToOneField(Image, on_delete=models.CASCADE, related_name='image_binary')
    binary = models.BinaryField()
    content_type = models.CharField(max_length=DEFAULT_MAX_LENGTH)
