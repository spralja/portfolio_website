from django.urls import path

from . import views

app_name = 'cv'
urlpatterns = [
    path('', views.index, name='index'),
    path('experiences', views.ExperienceAPIView.as_view(), name='ExperienceAPIView'),
    path('educations', views.EducationAPIView.as_view(), name='EducationAPIView'),
    path('cv', views.CVAPIView.as_view(), name='CVAPIView'),
]
