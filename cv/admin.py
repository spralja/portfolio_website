from django.contrib import admin

# Register your models here.
from .models import Experience, Date, Description

admin.site.register(Experience)
admin.site.register(Date)
admin.site.register(Description)
