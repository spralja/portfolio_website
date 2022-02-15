from django.http import HttpResponse
from django.template import loader

from .models import CV


def index(request, cv_name='main'):
    template = loader.get_template('cv/index.html')
    cv = CV.objects.filter(name=cv_name).first()
    context = {
        'cv': cv,
    }

    return HttpResponse(template.render(context, request))
