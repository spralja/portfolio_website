from django.db import models


# Create your models here.


class Experience(models.Model):
    authority = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
