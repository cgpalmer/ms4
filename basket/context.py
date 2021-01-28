from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from profiles.models import Image_upload


def basket_contents(request):

    basket_items = []
    minified_items = []
    total = 0
    full_price_total = 0
    products = Product.objects.filter(product_type="photo")
    user_photos = Image_upload.objects.all()
    product_count = 0
    delivery_total = 0
    basket = request.session.get('basket', {})
    are_all_items_linked = True
    multi_buy_message = ""

    if basket != {}:
        for item in basket['items']:
            product_count += 1
            product = get_object_or_404(Product, pk=item['item_id'])
            subtotal = product.discount_price * item['quantity']

            full_price_sub_total = product.price * item['quantity']

            if item['digital_download']:
                digital_download = "on"
            else:
                digital_download = None
                delivery_total += subtotal

            total += subtotal
            full_price_total += full_price_sub_total

            basket_items.append({
                'item': item,
                'product': product,
                'subtotal': subtotal,
                'digital_download': digital_download,
            })

            minified_items.append({
                'product_id': product.id,
                'quantity': item['quantity'],
                'subtotal': subtotal,
                'digital_download': digital_download,
            })

            list_of_linked_product_info = item['linked_products']
            for product_info in list_of_linked_product_info:
                if product_info == 'Not linked' and product.number_of_pictures > 0:
                    are_all_items_linked = False

    if delivery_total == 0 or total > settings.FREE_DELIVERY_AMOUNT:
        delivery = 0
        free_delivery_deficit = 0
    else:
        delivery = Decimal.from_float(settings.STANDARD_DELIVERY_AMOUNT)
        free_delivery_deficit = settings.FREE_DELIVERY_AMOUNT - delivery_total

    money_saved = full_price_total - total
    grand_total = delivery + total
    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_deficit': free_delivery_deficit,
        'FREE_DELIVERY_AMOUNT': settings.FREE_DELIVERY_AMOUNT,
        'grand_total': grand_total,
        'delivery_total': delivery_total,
        'are_all_items_linked': are_all_items_linked,
        'products': products,
        'user_photos': user_photos,
        'multi_buy_message': multi_buy_message,
        'money_saved': money_saved,
        'minified_items': minified_items
    }

    return context
