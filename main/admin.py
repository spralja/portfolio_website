from django.contrib import admin

from .models import User, Picture, Social, Project, Remote, StaticFile

admin.site.register(User)
admin.site.register(Picture)
admin.site.register(Social)
admin.site.register(Project)


class RemoteAdmin(admin.ModelAdmin):
    readonly_fields = ('last_accessed',)
    
admin.site.register(Remote, RemoteAdmin)

admin.site.register(StaticFile)
