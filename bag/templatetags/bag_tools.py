from django import template

register = template.Library()

@register.simple_tag
def example_tag():
    return "This is an example tag"


@register.filter
def calc_subtotal(value, quantity):
    return value * quantity  # Assuming you want to multiply price by quantity