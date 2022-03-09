from django.urls import path

from . import views

app_name = 'image_server'
urlpatterns = [
    path('<str:uid>/', views.get_image, name='image'),
]
