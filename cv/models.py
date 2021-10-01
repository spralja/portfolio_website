from django.db import models


# Create your models here.


class Experience(models.Model):
    authority = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    hide = models.BooleanField(default=False)

    def __str__(self):
        return "%s - %s" % (self.authority, self.title)

