from django.db import models

DEFAULT_MAX_LENGTH = 255


class Repository(models.Model):
    organisation = models.CharField(max_length=DEFAULT_MAX_LENGTH)
    repository = models.CharField(max_length=DEFAULT_MAX_LENGTH)
    hook_id = models.CharField(max_length=DEFAULT_MAX_LENGTH, null=True, blank=True)

    @property
    def origin(self):
        return f'https://github.com/{self.organisation}/{self.repository}'

    def __str__(self):
        return self.origin
