from rest_framework.serializers import *
from markdown import markdown
 

class MarkdownField(CharField):
    def to_representation(self, obj):
        return {'title': obj.title, 'description': markdown(obj.description)}