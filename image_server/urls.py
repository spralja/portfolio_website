from django.urls import path

from . import views

app_name = 'image_server'
urlpatterns = [
    path('<str:uid>/', views.get_image, name='image'),
    path('__future__/<str:uid>/', views.__future__get_image, name='__future__.get_image')
]

