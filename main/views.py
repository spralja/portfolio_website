from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import redirect

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User, Project
from .serializers import ExperienceSerializer, EducationSerializer, CVSerializer


def index(request):
    template = loader.get_template('main/index.html')
    user = User.objects.first()
    context = {
        'user': user,
    }

    return HttpResponse(template.render(context, request))


def contact(request):
    template = loader.get_template('main/contact.html')
    user = User.objects.first()

    context = {
        'user': user,
    }

    return HttpResponse(template.render(context, request))


def project(request, name):
    static_website = Project.objects.filter(name=name).first().static_website
    return redirect(static_website.get_url())

class ProjectAPIView(APIView):
    def get(serf, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


class ExperienceAPIView(APIView):
    def get(self, request, name='main'):
        experiences = CV.objects.filter(name=name).first().experiences.all()
        serializer = ExperienceSerializer(experiences, many=True)
        return Response(serializer.data)


class EducationAPIView(APIView):
    def get(self, request, name='main'):
        educations = CV.objects.filter(name=name).first().educations.all()
        print(educations)
        serializer = EducationSerializer(educations, many=True)
        return Response(serializer.data)


class CVAPIView(APIView):
    def get(self, request, name='main'):
        cv = CV.objects.filter(name=name).first()
        serializer = CVSerializer(cv)
        return Response(serializer.data)


