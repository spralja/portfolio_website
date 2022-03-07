from django.urls import path

from . import views

app_name = 'github_integration'
urlpatterns = [
    path('hooks/<str:repository>/', views.hooks, name='hooks'),
]

