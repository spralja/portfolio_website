from rest_framework.serializers import *
from markdown import markdown
 

class MarkdownField(CharField):
    def to_representation(self, value):
        return markdown.markdown(value)