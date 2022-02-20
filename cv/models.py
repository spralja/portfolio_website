from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

DEFAULT_MAX_LENGTH = 255


def HasParent(cls, *, related_name, on_delete=models.CASCADE, **options):
    Meta = type(related_name + 'Meta', (), {
        'abstract': 'True',
    })

    return type(related_name, (models.Model,), {
        'parent': models.ForeignKey(cls, on_delete=on_delete, related_name=related_name, **options),
        'Meta': Meta,
        '__module__': __name__,
    })


class HasShown(models.Model):
    shown = models.BooleanField(default=True)

    class Meta:
        abstract = 'True'


class UserPicture(models.Model):
    url = models.URLField()
    alt = models.CharField(max_length=DEFAULT_MAX_LENGTH)

    def __str__(self):
        return self.alt


class Resume(models.Model):
    heading = models.CharField(max_length=DEFAULT_MAX_LENGTH, primary_key=True)

    class Meta:
        verbose_name = 'Résumé'

    def __str__(self):
        return self.heading


class CV(models.Model):
    name = models.CharField(max_length=DEFAULT_MAX_LENGTH, primary_key=True, default='main')
    user_name = models.CharField(max_length=DEFAULT_MAX_LENGTH)
    user_picture = models.ForeignKey(UserPicture, on_delete=models.CASCADE)
    github = models.URLField()
    linkedin = models.URLField()
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Experience(HasParent(CV, related_name='experiences')):
    authority = models.CharField(max_length=DEFAULT_MAX_LENGTH)
    title = models.CharField(max_length=DEFAULT_MAX_LENGTH)
    start_time = models.DateField()
    end_time = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.authority} - {self.title}"

    def get_time_frame(self):
        return f"{self.start_time.strftime('%B %Y')} - " \
               f"{self.end_time.strftime('%B %Y') if self.end_time is not None else ''}"


class Description(HasParent(Experience, related_name='descriptions')):
    description = models.CharField(max_length=DEFAULT_MAX_LENGTH)

    def __str__(self):
        return self.description


class Education(HasParent(CV, related_name='educations')):
    authority = models.CharField(max_length=DEFAULT_MAX_LENGTH)
    title = models.CharField(max_length=DEFAULT_MAX_LENGTH)
    major = models.CharField(max_length=DEFAULT_MAX_LENGTH)
    gpa = models.FloatField(validators=[MinValueValidator(-3.0), MaxValueValidator(12.0)])
    start_time = models.DateField()
    end_time = models.DateField()

    def __str__(self):
        return f"{self.authority} - {self.title}"

    def get_time_frame(self):
        return f"{self.start_time.strftime('%B %Y')} - " \
               f"{self.end_time.strftime('%B %Y') if self.end_time is not None else ''}"


class Course(HasParent(Education, related_name='courses')):
    name = models.CharField(max_length=DEFAULT_MAX_LENGTH)
    description = models.CharField(max_length=DEFAULT_MAX_LENGTH)

    def __str__(self):
        return f"{self.name} - {self.description}"


class Project(HasParent(Education, related_name='projects')):
    title = models.CharField(max_length=DEFAULT_MAX_LENGTH)

    class Meta:
        unique_together = ('parent', 'title')

    def __str__(self):
        return self.title


class TechnicalSkill(HasParent(CV, related_name='technical_skills'), models.Model):
    name = models.CharField(max_length=DEFAULT_MAX_LENGTH)

    class Meta:
        unique_together = ('parent', 'name')

    def __str__(self):
        return self.name


class Language(HasParent(CV, related_name='languages')):
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

    level = models.IntegerField(choices=Level.choices)
    name = models.CharField(max_length=DEFAULT_MAX_LENGTH)

    class Meta:
        unique_together = ('parent', 'name')

    def __str__(self):
        return f"{self.name} - {self.get_level()}"

    def get_level(self):
        return self.switch_level[self.level]


class Hobby(HasParent(CV, related_name='hobbies')):
    name = models.CharField(max_length=DEFAULT_MAX_LENGTH)

    class Meta:
        verbose_name_plural = 'Hobbies'
        unique_together = ('parent', 'name')

    def __str__(self):
        return self.name


class Paragraph(HasParent(Resume, related_name='paragraphs')):
    paragraph = models.TextField()

    def __str__(self):
        return self.paragraph
