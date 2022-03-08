from django.http import HttpResponse
from .models import Project

def index(request, project_name):

    return HttpResponse(project_name)

def image(request, project_name, image_name):
    image = Project.objects.filter(name=project_name).first().images.filter(name=image_name).first()
    valid_image = str(image.image)
    try:
        with open(valid_image, "rb") as f:
            return HttpResponse(f.read(), content_type="image/jpeg")
    except IOError:
        red = Image.new('RGBA', (1, 1), (255,0,0,0))
        response = HttpResponse(content_type="image/jpeg")
        red.save(response, "JPEG")
        return response
        
