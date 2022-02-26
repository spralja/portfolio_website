from django.urls import path

from . import views

app_name = 'path_finding_algorithms'
urlpatterns = [
    path('', views.index, name='index'),
]

