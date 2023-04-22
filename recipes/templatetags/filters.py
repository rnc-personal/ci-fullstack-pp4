from django import template

register = template.Library()

@register.filter
def less_than(value, arg):
    try:
        return value < arg
    except (ValueError, TypeError):
        return False

@register.filter
def greater_than(value, arg):
    try:
        return value > arg
    except (ValueError, TypeError):
        return False
