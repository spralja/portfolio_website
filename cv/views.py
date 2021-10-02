from django.http import HttpResponse
from django.template import loader

from cv.models import Experience, Description, Education, Course, Project


def index(request):
    template = loader.get_template('cv/index.html')
    context = {
        'experiences': Experience.objects.order(),
        'descriptions': Description.objects.all(),
        'educations': Education.objects.all(),
        'courses': Course.objects.all(),
        'projects': Project.objects.all(),
    }
    return HttpResponse(template.render(context, request))
