from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Date(models.Model):
    class Month(models.IntegerChoices):
        JANUARY = 1, _("January")
        FEBRUARY = 2, _("February")
        MARCH = 3, _("March")
        APRIL = 4, _("April")
        MAY = 5, _("May")
        JUNE = 6, _("June")
        JULY = 7, _("July")
        AUGUST = 8, _("August")
        SEPTEMBER = 9, _("September")
        OCTOBER = 10, _("October")
        NOVEMBER = 11, _("November")
        DECEMBER = 12, _("December")

        def __str__(self):
            return self.label

    month = models.IntegerField(choices=Month.choices)
    year = models.IntegerField()

    def __str__(self):
        return "%s/%s" % (self.month, self.year)

    def compare(self, other):
        if self.year == other.year:
            return self.month - other.month

        return self.year - other.year


class ExperienceManager(models.Manager):
    def order(self, *args, **kwargs):
        qs = self.get_queryset().filter(*args, **kwargs)
        return sorted(qs, key=lambda n: (n[0] , int(n[1:])))


class Experience(models.Model):
    authority = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    start_date = models.ForeignKey(Date, on_delete=models.CASCADE, related_name="start_date")
    end_date = models.ForeignKey(Date, on_delete=models.CASCADE, blank=True, null=True, related_name="end_date")

    def __str__(self):
        return "%s - %s" % (self.authority, self.title)

    def get_time_frame(self):
        string = "%s - " % self.start_date
        if self.end_date is not None:
            string += self.end_date.__str__()

        return string

    def compare(self, other):
        if self.end_date is None:
            if other.end_date is None :
                if self.start_date.year == other.start_date.year:
                    return self.start_date.month - other.start_date.month


class Description(models.Model):
    description = models.CharField(max_length=200)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
