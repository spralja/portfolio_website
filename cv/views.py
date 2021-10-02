from django.http import HttpResponse
from django.template import loader

from cv.models import Experience, Description


def index(request):
    template = loader.get_template('cv/index.html')
    context = {
        'experiences': Experience.objects.order(),
        'descriptions': Description.objects.all(),
    }
    return HttpResponse(template.render(context, request))
