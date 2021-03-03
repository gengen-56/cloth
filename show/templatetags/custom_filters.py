from django import template

register = template.Library()


@register.filter
def season_checked(value, querydict):
    seasons = querydict.getlist('season')
    if str(value) in seasons:
        return "season_checked"
    return ""


@register.filter
def checked(value, querydict):
    parts = querydict.getlist('part')
    if str(value) in parts:
        return "checked"
    return ""
