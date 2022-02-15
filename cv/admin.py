from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Experience)
admin.site.register(Description)
admin.site.register(Education)
admin.site.register(Project)
admin.site.register(Course)
admin.site.register(TechnicalSkill)
admin.site.register(Language)
admin.site.register(Hobby)
admin.site.register(CV)
admin.site.register(UserPicture)

