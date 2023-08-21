from decimal import Decimal
from django.conf import settings

def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0

    # Calculate total and product_count based on bag contents
    for item in bag_items:
        total += item.price * item.quantity
        product_count += item.quantity

    if total < settings.FREE_MEMBERS_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_MEMBERS_THRESHOLD - total
    else: 
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count, 
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_members_threshold': settings.FREE_MEMBERS_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
