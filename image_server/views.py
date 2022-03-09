from .models import Image

from django.http import HttpResponse


def get_image(request, uid):
    image = Image.objects.filter(uid=uid).first()
    if image is None:
        return HttpResponse('404 Not Found!')
    
    return HttpResponse(image.image_binary.binary, image.image_binary.content_type)