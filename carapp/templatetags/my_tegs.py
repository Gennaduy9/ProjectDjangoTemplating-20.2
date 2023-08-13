from django import template
from django.conf import settings

register = template.Library()

# @register.filter()
# def mediapath(val):
#     if val:
#         return f'/media/{val}'
#
#     return '#'
#
# @register.simple_tag
# def mediapath(path):
#     return '/media/' + str(path)

@register.filter
def mediapath(image_path):
    return f"{settings.MEDIA_URL}{image_path}"
