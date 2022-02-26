from django.http import HttpResponse, Http404
from django.template import loader

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User, Project, Html, Static
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
    project = Project.objects.filter(name=name).first()
    index = Html.objects.filter(project=project).first()
    if index:
        return HttpResponse(index.index)

    index = project.get_index()
    
    Html.objects.create(project=project, index=index)
    return HttpResponse(index)

def static(request, name, static):
    project = Project.objects.filter(name=name).first()
    index = Static.objects.filter(project=project, name=static).first()
    if index:
        return HttpResponse(index.static, content_type='application/javascript')

    index = project.get_static(static)
    Static.objects.create(project=project, name=static, static=index)
    return HttpResponse(index)



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


