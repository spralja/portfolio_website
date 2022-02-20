from django.http import HttpResponse, Http404
from django.template import loader

from .models import CV


def index(request, cv_name='main'):
    template = loader.get_template('cv/index.html')
    cv = CV.objects.filter(name=cv_name).first()
    if cv is None:
        raise Http404('Cv does not exist')

    context = {
        'cv': cv,
    }

    return HttpResponse(template.render(context, request))
