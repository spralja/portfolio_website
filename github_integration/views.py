from django.http import HttpResponse

# Create your views here.

def hooks(request, repository):
    print(request)
    print(vars(request))
    print([f'{key}: {value}' for key, value in vars(request).items()])
    return HttpResponse('', status=202)
