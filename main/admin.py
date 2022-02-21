from django.contrib import admin

from .models import *

admin.site.register(User)

admin.site.register(CV)
admin.site.register(Picture)
admin.site.register(Resume)
admin.site.register(Paragraph)


admin.site.register(Experience)
admin.site.register(Description)
admin.site.register(Education)
admin.site.register(Project)
admin.site.register(Course)

admin.site.register(TechnicalSkill)
admin.site.register(Language)
admin.site.register(Hobby)

