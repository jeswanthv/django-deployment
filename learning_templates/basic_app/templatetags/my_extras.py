from django import template

register = template.Library()

def cut(value,arg):
    """
    THis cuts the arg
    """
    return value.replace(arg,'')

register.filter('cut',cut)
