from django.db import models

# Create your models here.


class Experience(models.Model):
    authority = models.charField(max_length=200)
    start_date = models.dateTimeField('date started')
    end_date = models.dateTimeField('date finished')
    description = models.
