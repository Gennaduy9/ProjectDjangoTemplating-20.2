from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def mediapath(path):
    return '/media/' + str(path)

