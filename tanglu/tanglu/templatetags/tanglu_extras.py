from django import template

register = template.Library()

def safewrap(val, arg):
    return val.format(arg)

register.filter('safewrap', safewrap) 
safewrap.is_safe = True
