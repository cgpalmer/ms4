from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.FREE_DELIVERY_AMOUNT:
        delivery = Decimal.from_float(settings.STANDARD_DELIVERY_AMOUNT)
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
