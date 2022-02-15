from django.http import HttpResponse
from django.template import loader

from .models import CV

from django.db import models


def cv_dict(cv_name='main'):
    cv = CV.objects.filter(name=cv_name).first()
    dct = {}
    for field in CV._meta.get_fields():
        if type(field) is models.ManyToOneRel:
            dct[field.name] = list((getattr(cv, field.name)).all())
        else:
            dct[field.name] = getattr(cv, field.name)

    return dct


def index(request, cv_name='main'):
    template = loader.get_template('cv/index.html')
    cv = CV.objects.filter(name=cv_name).first()
    context = {
        'cv': cv,
    }
    return HttpResponse(template.render(context, request))
