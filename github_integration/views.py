from django.shortcuts import render

# Create your views here.

def hooks(request, repository):
    print(request)
    print(vars(request))
    print([f'{key}: {value}' for key, value in vars(request).items()])
