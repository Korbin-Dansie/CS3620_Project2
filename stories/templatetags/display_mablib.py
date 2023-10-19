from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def display_mablig(story, answer):
    something = '%s<span class="bold">%s</span>' % (story, answer)
    return something
