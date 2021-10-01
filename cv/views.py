from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('cv/index.html')
    return HttpResponse(template.render({}, request))
