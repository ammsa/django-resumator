from django import template
import resumator

register = template.Library()


@register.simple_tag
def get_version():
    return resumator.__version__
