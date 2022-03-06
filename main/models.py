from django.core.validators import MaxValueValidator, MinValueValidator
from portfolio_website import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.template import Context, Template
from datetime import datetime

from markdown import markdown
from github import Github
from github.Commit import Commit

from portfolio_website.settings import TIME_ZONE, GITHUB_API_TOKEN

DEFAULT_MAX_LENGTH = 255


class Picture(models.Model):
    url = models.URLField()
    alt = models.CharField(max_length=DEFAULT_MAX_LENGTH)

    def __str__(self):
        return self.alt


class User(models.Model):
    name = models.CharField(max_length=DEFAULT_MAX_LENGTH)
    about_me = models.TextField(blank=True)
    picture = models.OneToOneField(Picture, on_delete=models.CASCADE, null=True)
    email = models.EmailField(null=True)
    github = models.URLField(null=True)
    gitlab = models.URLField(null=True)
    linkedin = models.URLField(null=True)

    def __str__(self):
        return self.name


class Social(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='socials')
    title = models.CharField(max_length=DEFAULT_MAX_LENGTH)
    url = models.URLField()
    class Meta:
        unique_together = ('user', 'title')


class Project(models.Model):
    user = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=DEFAULT_MAX_LENGTH)
    name = models.CharField(max_length=DEFAULT_MAX_LENGTH, primary_key=True)
    _description = models.MarkdownField(blank=True)

    def __str__(self):
        return self.title

    @property
    def description(self):
        template = Template(markdown(self._description))
        context = Context({'self': self})
        return template.render(context)


class Remote(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    organisation = models.CharField(max_length=DEFAULT_MAX_LENGTH)
    repository = models.CharField(max_length=DEFAULT_MAX_LENGTH)
    branch = models.CharField(max_length=DEFAULT_MAX_LENGTH, default='main')
    last_accessed = models.DateTimeField(default=datetime.fromtimestamp(0))

    def __str__(self):
        return str(self.organisation) + '/' + str(self.repository) + '@' + str(self.branch)

    def collect(self, name='index.html'):
        g = Github(*((GITHUB_API_TOKEN,) if GITHUB_API_TOKEN else ()))
        repository = g.get_user(self.organisation).get_repo(self.repository)
        if not repository.get_commits(since=self.last_accessed).totalCount:
            return self.static_files.filter(name=name).first()
        
        self.last_accessed = datetime.now()
        self.save()
        files = [git_tree_element.path for git_tree_element in repository.get_git_tree(f'{self.branch}?recursive=1').tree]

        for file in files:
            self.static_files.create(
                remote=self, 
                name=file, 
                content=repository.get_contents(file).decoded_content.decode()
            )
        
        return self.static_files.filter(name=name).first()


class StaticFile(models.Model):
    remote = models.ForeignKey(Remote, on_delete=models.CASCADE, related_name='static_files')
    name = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.remote.project.name + '/' + self.name

    @property
    def content_type(self):
        if self.name.split('.')[-1] == 'js':
            return 'application/javascript'
        
        if self.name.split('.')[-1] == 'css':
            return 'text/css'

        if self.name.split('.')[-1] in ('html', 'htm'):
            return 'text/html'

    class Meta:
        unique_together = ('remote', 'name')


def HasParent(cls, *, related_name,on_delete=models.CASCADE, **options):
    Meta = type(related_name + 'Meta', (), {
        'abstract': 'True',
    })

    return type(related_name, (models.Model,), {
        cls.__name__.lower(): models.ForeignKey(cls, on_delete=on_delete, related_name=related_name, **options),
        'Meta': Meta,
        '__module__': __name__,
    })


class HasShown(models.Model):
    shown = models.BooleanField(default=True)

    class Meta:
        abstract = 'True'





class Resume(HasParent(User, related_name='resumes')):
    heading = models.CharField(max_length=DEFAULT_MAX_LENGTH, primary_key=True)

    class Meta:
        verbose_name = 'Résumé'

    def __str__(self):
        return self.heading


class Experience(HasParent(User, related_name='experiences')):
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
    description = models.TextField(primary_key=True)

    def __str__(self):
        return self.description


class Education(HasParent(User, related_name='educations')):
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
    name = models.CharField(primary_key=True, max_length=DEFAULT_MAX_LENGTH)

    def __str__(self):
        return self.name





class TechnicalSkill(HasParent(User, related_name='technical_skills', null=True), models.Model):
    name = models.CharField(max_length=DEFAULT_MAX_LENGTH)

    def __str__(self):
        return self.name


class Language(HasParent(User, related_name='languages', null=True)):
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



    def __str__(self):
        return f"{self.name} - {self.get_level()}"

    def get_level(self):
        return self.switch_level[self.level]


class Hobby(HasParent(User, related_name='hobbies', null=True)):
    name = models.CharField(max_length=DEFAULT_MAX_LENGTH)

    class Meta:
        verbose_name_plural = 'Hobbies'

    def __str__(self):
        return self.name


class Paragraph(HasParent(Resume, related_name='paragraphs')):
    paragraph = models.TextField()

    def __str__(self):
        return self.paragraph


class CV(HasParent(User, related_name='cvs')):
    name = models.CharField(max_length=DEFAULT_MAX_LENGTH, primary_key=True, default='main')
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    technical_skills = models.ManyToManyField(TechnicalSkill, blank=True)
    languages = models.ManyToManyField(Language, blank=True)
    hobbies = models.ManyToManyField(Hobby, blank=True)
    educations = models.ManyToManyField(Education, blank=True)
    experiences = models.ManyToManyField(Experience, blank=True)

    class Meta:
        verbose_name = 'Curriculum Vitae'
        verbose_name_plural = 'Curricula Vitae'

    def __str__(self):
        return self.name
