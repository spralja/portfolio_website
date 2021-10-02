from django.contrib import admin

# Register your models here.
from .models import Experience, Date, Description, Education, Project, Course

admin.site.register(Experience)
admin.site.register(Date)
admin.site.register(Description)
admin.site.register(Education)
admin.site.register(Project)
admin.site.register(Course)