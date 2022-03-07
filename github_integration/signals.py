from portfolio_website.settings import GITHUB_API_TOKEN, DOMAIN

from .models import Repository

from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from git import Repo
from pathlib import Path
from github import Github
import requests

GIT_PYTHON_PATH = Path(__file__).parent / '.GitPython'


@receiver(post_save, sender=Repository)
def repository_post_save(sender, instance, created, **kwargs):
    
    if not created:
        return

    if type(instance) is not Repository:
        return

    hook_url = f'{DOMAIN}/github/{instance.repository}'

    #if GIT_PYTHON_PATH.is_dir():
        #return

    #repo = Repo.clone_from(instance.origin, GIT_PYTHON_PATH)

    g = Github(*((GITHUB_API_TOKEN,) if GITHUB_API_TOKEN else ()))
    repository = g.get_user(instance.organisation).get_repo(instance.repository)
    hooks = repository.get_hooks()
    for hook in hooks:
        if hook.config['url'] == hook_url:
            instance.hook_id = hook.id
            instance.save()
            return

    hook = repository.create_hook(
        'web', 
        {
            'content_type': 'json',
            'insecure_ssl': '0',
            'url': hook_url,
        },
    )

    instance.hook_id = hook.id
    instance.save()


@receiver(pre_delete, sender=Repository)
def repository_pre_delete(sender, instance, **kwargs):
    if type(instance) is not Repository:
        return
    
    g = Github(*((GITHUB_API_TOKEN,) if GITHUB_API_TOKEN else ()))
    repository = g.get_user(instance.organisation).get_repo(instance.repository)
    try:
        hook = repository.get_hook(instance.hook_id)
        hook.delete()
    except:
        pass
