from django.http import HttpResponse
from django.template import loader

from cv.models import Experience


def index(request):
    template = loader.get_template('cv/index.html')
    context = {'experiences': Experience.objects.all()}
    return HttpResponse(template.render(context, request))
