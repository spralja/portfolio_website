from portfolio_website.settings import GITHUB_API_TOKEN

from .models import Repository

from django.db.models.signals import post_save
from django.dispatch import receiver

from git import Repo
from pathlib import Path
from github import Github
import requests

GIT_PYTHON_PATH = Path(__file__).parent / '.GitPython'


@receiver(post_save, sender=Repository)
def repository_post_save(sender, instance, created, **kwargs):
    print(f'sender: {sender}')
    print(f'instance: {instance}')
    print(f'created: {created}')
    print(f'kwargs: {kwargs}')
    print()
    if type(instance) is not Repository:
        return

    #if GIT_PYTHON_PATH.is_dir():
        #return

    #repo = Repo.clone_from(instance.origin, GIT_PYTHON_PATH)

    g = Github(*((GITHUB_API_TOKEN,) if GITHUB_API_TOKEN else ()))
    repository = g.get_user(instance.organisation).get_repo(instance.repository)
    hooks = repository.get_hooks()
    for hook in hooks:
        if hook.config['url'] == 'https://spralja-portfolio.azurewebsites.net/':
            return

    hook = repository.create_hook(
        'web', 
        {
            'content_type': 'json',
            'insecure_ssl': '0',
            'url': 'https://spralja-portfolio.azurewebsites.net/'
        },
    )

    instance.hook_id = hook.id
