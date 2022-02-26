from django.contrib import admin

from .models import User, Picture, Project, Remote, StaticWebsite

admin.site.register(User)
admin.site.register(Picture)
admin.site.register(Project)
admin.site.register(Remote)
admin.site.register(StaticWebsite)
