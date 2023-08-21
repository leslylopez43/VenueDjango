from decimal import Decimal
from django.conf import settings

def bag_contents(request):

    bag_item =[]
    total = 0
    product_count = 0

    if total< settings.FREE_MEMBERS_THRESHOLD:
        delivery = total * Decimal(settings.STANDARS_MEMEBERS_PORCENTAGE/100)
        free_delivery_delta = FREE_MEMBERS_THRESHOLD - total
    else: 
        delivery =0
        free_delivery_delta = 0

    grand_total = delivery + total




    context={
         'bag_items' : bag_items,
         'total': total,
         'product_count': product_count 
         'delivery': delivery,
         'free_delivery_delta': free_delivery_delta
         'free_members_thresehold': settings.FREE_MEMBERS_THRESHOLD,
         'grand_total': grand_total,
         }


    return context 