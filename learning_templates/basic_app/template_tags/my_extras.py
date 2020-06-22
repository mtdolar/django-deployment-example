from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    cuts all values of "arg"
    """
    return value.replace(arg,'')

#register.filter('cut',cut)
