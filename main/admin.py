from django.contrib import admin

from .models import User, Picture, Project

admin.site.register(User)

admin.site.register(Project)

class PictureAdmin(admin.ModelAdmin):
    list_display = ('url', 'alt')
    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True

admin.site.register(Picture, PictureAdmin)
