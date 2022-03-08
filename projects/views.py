from django.http import HttpResponse
from .models import Image


def image(request, image_name):
    image = Image.objects.filter(name=image_name).first()
    valid_image = str(image.image)
    try:
        with open(valid_image, "rb") as f:
            return HttpResponse(f.read(), content_type="image/jpeg")
    except IOError:
        red = Image.new('RGBA', (1, 1), (255,0,0,0))
        response = HttpResponse(content_type="image/jpeg")
        red.save(response, "JPEG")
        return response
        
