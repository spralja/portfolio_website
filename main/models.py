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

    def __str__(self):
        return self.name


class Social(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='socials')
    title = models.CharField(max_length=DEFAULT_MAX_LENGTH)
    url = models.URLField()

    class Meta:
        unique_together = ('user', 'title')

    def __str__(self):
        return self.title


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
