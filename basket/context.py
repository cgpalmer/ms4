from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0
    delivery_total = 0
    basket = request.session.get('basket', {})
    are_all_items_linked = True
    
    if basket != {}:
        for item in basket['items']:
            product = get_object_or_404(Product, pk=item['item_id'])
            # You were dealing with the delivery
            subtotal = item['quantity'] * product.price
            digital_download = "Delivery"
            if item['digital_download']:
                digital_download = "Yes"
            else:
                digital_download = "Delivery"
                delivery_total += subtotal

            total += subtotal

            basket_items.append({
                'item': item,
                'product': product,
                'subtotal': subtotal,
                'digital_download': digital_download,
                
            })

          
           
            list_of_linked_product_info = item['linked_products']
            print("LIST " + str(list_of_linked_product_info))
            for product_info in list_of_linked_product_info:
                print(product_info[0])
                if product_info == ['Not linked'] and product.number_of_pictures > 0:
                    are_all_items_linked = False
                    print(are_all_items_linked)


            
   

    if delivery_total == 0 or total > settings.FREE_DELIVERY_AMOUNT:
        print(delivery_total)
        print(total)
        delivery = 0
        free_delivery_deficit = 0
    else:
        delivery = Decimal.from_float(settings.STANDARD_DELIVERY_AMOUNT)
        free_delivery_deficit = settings.FREE_DELIVERY_AMOUNT - total
    
    
    grand_total = delivery + total
    
    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_deficit': free_delivery_deficit,
        'FREE_DELIVERY_AMOUNT': settings.FREE_DELIVERY_AMOUNT,
        'grand_total': grand_total,
        'new_customer_offer': settings.NEW_CUSTOMER_OFFER,
        'delivery_total': delivery_total,
        'are_all_items_linked': are_all_items_linked
        
      
    }

    return context
