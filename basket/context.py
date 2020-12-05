from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product, Image_upload
import math

def basket_contents(request):

    basket_items = []
    total = 0
    products = Product.objects.filter(product_type="photo")
    user_photos = Image_upload.objects.all()
    product_count = 0
    delivery_total = 0
    basket = request.session.get('basket', {})
    are_all_items_linked = True
    multi_buy_message = ""
    
    multi_buy_items_in_basket = []
    print("MULTI BUY")
    
    if basket != {}:
        for item in basket['items']:
            
            product = get_object_or_404(Product, pk=item['item_id'])
            print("Reached")
            print(product.special_offer)
            # Handling the multi-buy issues
            if str(product.special_offer) == 'multi-buy':
                print("******* Multi-buy offer *******")
                print(item['quantity'])
                if item['quantity'] < 3:
                    number_of_discounts_to_apply = 0
                    subtotal = item['quantity'] * product.price
                elif item['quantity'] == 3:
                    number_of_discounts_to_apply = 1
                    subtotal = item['quantity'] * product.discount_price
                else:
                    number_of_discounts_to_apply = math.floor(int(item['quantity'] / 3))
                    print(number_of_discounts_to_apply)
                    products_at_normal_price = int(item['quantity']) - (number_of_discounts_to_apply * 3)
                    print(products_at_normal_price)
                    discounted_sub_price = (number_of_discounts_to_apply * 3) * product.discount_price
                    print(discounted_sub_price)
                    sub_price = products_at_normal_price * product.price
                    print(sub_price)
                    subtotal = discounted_sub_price + sub_price                            
                    print(subtotal)
               
                # # write modolus code here for the messages
            else:
                subtotal = item['quantity'] * product.discount_price
            
            

            # You were dealing with the delivery
            # print(product.special_offer)
            # if str(product.special_offer) != "multi-buy":
            #     subtotal = item['quantity'] * product.discount_price
            # else:
            #     if number_of_discounts_to_apply == 0:
            #         subtotal = item['quantity'] * product.price
            #     elif number_of_discounts_to_apply == 1:
            #         subtotal = (item['quantity'] * product.price) * product.discount_price
            #     else:
            #         products_at_normal_price = int(item['quantity']) - (number_of_discounts_to_apply * 3)
            #         print(products_at_normal_price)
            #         discounted_sub_price = number_of_discounts_to_apply * product.discount_price
            #         print(discounted_sub_price)
            #         sub_price = products_at_normal_price * product.price
            #         print(sub_price)
            #         subtotal = discounted_sub_price + sub_price                            
            #         print(subtotal)
            if item['digital_download']:
                digital_download = "on"
            else:
                digital_download = None
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
        'are_all_items_linked': are_all_items_linked,
        'products': products,
        'user_photos': user_photos,
        'multi_buy_message': multi_buy_message
      
    }

    return context
