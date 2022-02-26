from django.contrib import admin

from .models import User, Picture, Project

admin.site.register(User)
admin.site.register(Picture)
admin.site.register(Project)
