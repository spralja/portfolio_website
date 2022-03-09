from django.contrib import admin

from .models import Image, ImageBinary

admin.site.register(Image)
admin.site.register(ImageBinary)
