from django import template
register=template.Library()
@register.filter
def Str(r):
    return str(r)
