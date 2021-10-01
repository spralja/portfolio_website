from django.urls import path

from . import views

app_name = 'cv'
urlpatterns = [
    path('cv', views.index, name='index')
]