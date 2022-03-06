from django.http import HttpResponse, Http404
from django.template import loader

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User, Project


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


def project(request, name, subfile=''):
    remote = Project.objects.filter(name=name).first().remote
    index = remote.collect(*((subfile, ) if subfile else ())) 
    return HttpResponse(index.content, content_type=index.content_type)
