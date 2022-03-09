from django.apps import AppConfig
from django.db.models.signals import post_save, pre_delete


class ImageServerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'image_server'

    def ready(self):
        from . import signals
        pre_delete.connect(signals.image_pre_delete, dispatch_uid='image_server.signals.image_pre_delete')
        post_save.connect(signals.create_image_binary, dispatch_uid='image_server.signals.create_image_binary')
