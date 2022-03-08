from .models import Image

from django.http import HttpResponse


def get_image(request, uid):
    image = Image.objects.filter(uid=uid).first()
    if image is None:
        return HttpResponse('404 Not Found!')
    try:
        return HttpResponse(image.get_raw(), image.get_content_type())
    except (ValueError, IOError) as e:
        return HttpResponse(str(e))
