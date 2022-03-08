from .models import Image

from django.db.models.signals import pre_delete
from django.dispatch import receiver

from pathlib import Path


@receiver(pre_delete, sender=Image, dispatch_uid='image_server.image_pre_delete')
def image_pre_delete(sender, instance, **kwargs):
    instance.path.unlink(missing_ok=True)
