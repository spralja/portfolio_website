from .models import Image, ImageBinary

from django.db.models.signals import post_save
from django.dispatch import receiver

from pathlib import Path


@receiver(post_save, sender=Image, dispatch_uid='image_server.signals.create_image_binary')
def create_image_binary(sender, instance, **kwargs):
    if sender is not Image:
        return

    if ImageBinary.objects.filter(image=instance):
        return

    ImageBinary.objects.create(
        image=instance,
        binary=instance.get_raw(),
        content_type=instance.get_content_type(),
    )

    instance.path.unlink(missing_ok=True)
