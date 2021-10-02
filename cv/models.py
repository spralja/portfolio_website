from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Date(models.Model):
    switch_month = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

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

    month = models.IntegerField(choices=Month.choices)
    year = models.IntegerField()

    def __str__(self):
        return "%s %s" % (self.get_month(), self.year)

    def get_month(self):
        return self.switch_month[self.month]

    def compare(self, other):
        if self.year == other.year:
            return self.month - other.month

        return self.year - other.year


class ExperienceManager(models.Manager):
    def order(self, *args, **kwargs):
        qs = self.get_queryset().filter(*args, **kwargs)
        return sorted(qs)


class Experience(models.Model):
    authority = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    start_date = models.ForeignKey(Date, on_delete=models.CASCADE, related_name="experience_start_date")
    end_date = models.ForeignKey(
        Date,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="experience_end_date"
    )

    objects = ExperienceManager()

    def __str__(self):
        return "%s - %s" % (self.authority, self.title)

    def get_time_frame(self):
        string = "%s - " % self.start_date
        if self.end_date is not None:
            string += self.end_date.__str__()

        return string

    def __lt__(self, other):
        return self.compare(other) > 0

    def compare(self, other):
        if self.end_date is None:
            if other.end_date is None:
                return self.start_date.compare(other.start_date)
            return 1

        if other.end_date is None:
            return -1

        if self.end_date.compare(other.end_date) == 0:
            return self.start_date.compare(other.start_date)

        return self.end_date.compare(other.end_date)


class Description(models.Model):
    description = models.CharField(max_length=200)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class Education(models.Model):
    authority = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    gpa = models.FloatField(validators=[MinValueValidator(-3.0), MaxValueValidator(12.0)])
    start_date = models.ForeignKey(Date, on_delete=models.CASCADE, related_name="education_start_date")
    end_date = models.ForeignKey(
        Date,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="education_end_date"
    )

    def __str__(self):
        return "%s - %s" % (self.authority, self.title)


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    education = models.ForeignKey(Education, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True, null=True)
    education = models.ForeignKey(Education, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class TechnicalSkill(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


'''class Language(models.Model):

    class Level(models.IntegerChoices):
        ELEMENTARY = 1, _("elementary")
        PROFESSIONAL = 2, _("professional")
        FLUENT = 3, _("fluent")
        BILINGUAL = 4, _("bilingual")
        NATIVE = 5, _("native")

    name = models.CharField(max_length=20, primary_key=True)
    level = models.IntegerField(choices=Level)'''


class Language(models.Model):
    switch_level = {
        1: "elementary",
        2: "professional",
        3: "fluent",
        4: "bilingual",
        5: "native",
    }

    class Level(models.IntegerChoices):
        ELEMENTARY = 1, _("elementary")
        PROFESSIONAL = 2, _("professional")
        FLUENT = 3, _("fluent")
        BILINGUAL = 4, _("bilingual")
        NATIVE = 5, _("native")

    level = models.IntegerField(choices=Level.choices)
    name = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return "%s - %s" %(self.name, self.get_level())

    def get_level(self):
        return self.switch_level[self.level]


class Hobby(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Hobbies"

    def __str__(self):
        return self.name
