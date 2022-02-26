from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:name>/', views.project, name='project'),
    path('<str:name>/<str:subfile>/', views.subfile, name='project'),
]

