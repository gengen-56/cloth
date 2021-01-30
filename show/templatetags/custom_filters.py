from django import template

register = template.Library()


@register.filter
def checked(value, querydict):
    parts = querydict.getlist('part')
    if str(value) in parts:
        return "checked"
    return ""


@register.filter
def name(querydict):
    name = querydict.get('name')

    return "" if name is None else name
