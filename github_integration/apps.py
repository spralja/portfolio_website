from django.apps import AppConfig
from django.db.models.signals import post_save

class GithubIntegrationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'github_integration'

    def ready(self):
        from . import signals
        post_save.connect(
            signals.repository_post_save, 
            dispatch_uid='github_integration.signals.git_repository_post_save'
        )
