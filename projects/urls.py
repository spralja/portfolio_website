from django.urls import path

from . import views

app_name = 'projects'
urlpatterns = [
    path('<str:project_name>/', views.index, name='index'),
    path('<str:project_name>/image/<str:image_name>/', views.image, name='image')
]
