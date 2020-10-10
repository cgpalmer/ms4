from decimal import Decimal
from django.conf import settings

def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0

    if total < settings.FREE_DELIVERY_AMOUNT:
        delivery = settings.STANDARD_DELIVERY_AMOUNT
        free_delivery_deficit = settings.FREE_DELIVERY_AMOUNT - total
    else:
        delivery = 0
        free_delivery_deficit = 0
    
    grand_total = delivery + total
    
    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_deficit': free_delivery_deficit,
        'FREE_DELIVERY_AMOUNT': settings.FREE_DELIVERY_AMOUNT,
        'grand_total': grand_total,
        'new_customer_offer': settings.NEW_CUSTOMER_OFFER
    }

    return context
