from django.contrib import admin

from .models import User, Picture, Project, StaticWebsite

admin.site.register(User)
admin.site.register(Picture)
admin.site.register(Project)
admin.site.register(StaticWebsite)
