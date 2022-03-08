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
        try:
            with open(self.path, 'rb') as file:
                return file.read()
        except IOError:
            raise IOError('image missing')

    def get_content_type(self):
        content_type = 'image/'
        file_extension = str(self.path).split('.')[-1]
        if file_extension in {'jpg', 'jpeg'}:
            content_type += 'jpeg'
        elif file_extension == 'png':
            content_type += 'png'
        else:
            raise ValueError('Unknown file extension')

        return content_type

    def __str__(self):
        return self.uid
