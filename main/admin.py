from django.contrib import admin

from .models import User, Picture, Project, Html, Static

admin.site.register(User)
admin.site.register(Picture)
admin.site.register(Project)
admin.site.register(Html)
admin.site.register(Static)