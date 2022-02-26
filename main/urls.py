from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('project/<str:name>/', views.project, name='project'),
    path('project/<str:name>/<str:static>/', views.static, name='project'),
]

