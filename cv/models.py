from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

class CV(models.Model):
    user_name = models.TextField()
    user_heading = models.TextField()
    

class TimeFrame(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class ExperienceManager(models.Manager):
    def order(self, *args, **kwargs):
        qs = self.get_queryset().filter(*args, **kwargs)
        return sorted(qs)


class Experience(models.Model):
    parent = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='cv_experience')
    authority = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    time_frame = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)

    objects = ExperienceManager()

    def __str__(self):
        return "%s - %s" % (self.authority, self.title)


class Description(models.Model):
    description = models.CharField(max_length=200)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class Education(models.Model):
    parent = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='cv_education')
    authority = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    gpa = models.FloatField(validators=[MinValueValidator(-3.0), MaxValueValidator(12.0)])
    time_frame = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.authority, self.title)

    def get_time_frame(self):
        string = "%s - " % self.start_date
        if self.end_date is None:
            return string

        string += "%s" % self.end_date
        return string


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    education = models.ForeignKey(Education, on_delete=models.CASCADE)

    def __str__(self):
        string = "%s" % self.name
        if self.description is None:
            return string

        return string + " - %s" % self.description


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True, null=True)
    education = models.ForeignKey(Education, on_delete=models.CASCADE)

    def __str__(self):
        string = "%s" % self.name
        if self.description is None:
            return string

        return string + " - %s" % self.description


class TechnicalSkill(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


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


class ResumeParagraph(models.Model):
    paragraph = models.TextField()

    def __str__(self):
        return self.paragraph
