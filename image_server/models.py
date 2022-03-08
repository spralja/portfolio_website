from portfolio_website.settings import BASE_DIR, DEFAULT_MAX_LENGTH

from django.db import models


class Image(models.Model):
    name = models.CharField(max_length=DEFAULT_MAX_LENGTH, primary_key=True)
    image = models.ImageField(upload_to=BASE_DIR / 'image_server' / 'storage')
