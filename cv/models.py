from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Experience(models.Model):
    authority = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    start_month = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    start_year = models.IntegerField()
    end_month = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)], blank=True, null=True)
    end_year = models.IntegerField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return "%s - %s" % (self.authority, self.title)

