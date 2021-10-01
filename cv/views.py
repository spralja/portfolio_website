from django.http import HttpRequest
from django.template import loader


def index(request):
    template = loader.get_template('cv/index')
    return HttpRequest(template.render({}, request))
