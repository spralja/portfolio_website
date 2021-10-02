from django.http import HttpResponse
from django.template import loader

from cv.models import Experience, Description, Education, Course, Project, TechnicalSkill, Language, Hobby


def index(request):
    template = loader.get_template('cv/index.html')
    context = {
        'experiences': Experience.objects.order(),
        'descriptions': Description.objects.all(),
        'educations': Education.objects.all(),
        'courses': Course.objects.all(),
        'projects': Project.objects.all(),
        'technical_skills': TechnicalSkill.objects.all(),
        'languages': Language.objects.all(),
        'hobbies': Hobby.objects.all(),
    }
    return HttpResponse(template.render(context, request))
