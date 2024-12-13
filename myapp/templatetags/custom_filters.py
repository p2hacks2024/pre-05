from django import template

register = template.Library()

@register.filter
def calc_top_position(counter):
    """Calculate the top position for store names"""
    return 130 + (counter * 40)
