from django import template

register = template.Library()


@register.filter
def get_attribute(obj, attr_name):
    """
    Custom template filter to get attribute value dynamically.
    Usage: {{ obj|get_attribute:attr_name }}
    """
    try:
        return getattr(obj, attr_name)
    except AttributeError:
        return None
