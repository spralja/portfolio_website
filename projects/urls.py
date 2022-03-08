from django.urls import path

from . import views

app_name = 'projects'
urlpatterns = [
    path('<str:image_name>/', views.image, name='image'),
]
