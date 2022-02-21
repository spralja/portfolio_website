from django.http import HttpResponse, Http404
from django.template import loader

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import CV
from .serializers import ExperienceSerializer, EducationSerializer, CVSerializer


def index(request, cv_name='main'):
    template = loader.get_template('main/index.html')
    cv = CV.objects.filter(name=cv_name).first()
    if cv is None:
        raise Http404('Cv does not exist')

    context = {
        'main': cv,
    }

    return HttpResponse(template.render(context, request))


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
