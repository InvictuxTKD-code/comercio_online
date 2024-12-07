
from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0

@register.filter
def thousand_separator(value):
    try:
        # Asegúrate de que el valor sea un número y convierte a entero si es necesario
        value = int(value)
        return "{:,}".format(value).replace(',', '.')
    except (ValueError, TypeError):
        return value
