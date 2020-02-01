from django import template

register = template.Library()

# Registers the cut filter function as "cut" (same name)
@register.filter()
def cut(value, arg):
    ''' Removes all values of arg from the given string (value) '''
    return value.replace(arg, "")