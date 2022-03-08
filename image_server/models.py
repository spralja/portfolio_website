from portfolio_website.settings import BASE_DIR, DEFAULT_MAX_LENGTH

from django.db import models

from pathlib import Path


class Image(models.Model):
    uid = models.CharField(max_length=DEFAULT_MAX_LENGTH, primary_key=True)
    image = models.ImageField(upload_to=Path('image_server') / 'storage', max_length=DEFAULT_MAX_LENGTH)

    @property
    def path(self):
        return Path(self.image.name)

    def __str__(self):
        return self.uid
