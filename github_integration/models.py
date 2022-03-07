from django.db import models

DEFAULT_MAX_LENGTH = 255



class Repository(models.Model):
    organisation = models.CharField(max_length=DEFAULT_MAX_LENGTH)
    repository = models.CharField(max_length=DEFAULT_MAX_LENGTH)
    hook_id = models.IntegerField(null=True, blank=True)

    @property
    def origin(self):
        return f'https://github.com/{self.organisation}/{self.repository}'

    def __str__(self):
        return self.origin


class Hook(models.Model):
    repository = models.OneToOneField(Repository, on_delete=models.CASCADE, related_name='hook')
    id = models.IntegerField(primary_key=True)
    ping_url = models.URLField()
