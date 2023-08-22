from django import template

register = template.library()

@register.filter(name='calc_subtotal')
def calc_subtotal (price, quantity):
    return price * quantity

# @register.filter
# def custom_filter(value):
#     # Your filter logic here
#     return value

# @register.tag
# def custom_tag(parser, token):
#     # Your tag logic here
#     return CustomNode()