from django import template

register = template.Library()

# Register -> Name, Function
@register.filter(name='cut')
#same as register.filter('cut', cut)
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string
    """
    return value.replace(arg,'')



