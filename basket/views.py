from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product, Image_upload
import uuid
# Create your views here.


def view_basket(request):
    # Returning the user's basket
    return render(request, 'basket/basket.html')

def add_to_basket(request, item_id):
    



    #adding to a basket
    basket = request.session.get('basket', {})
    basket_item_id = request.session.get('basket_item_id')
    print("item id from session" + str(basket_item_id))
    quantity = int(request.POST.get('quantity'))
    digital_download = request.POST.get('digital_download')
    print("digi downl " + str(digital_download))
    linked_products = [['Not linked']]
    # item id is passed through as parameter.
    #get the product
    product = get_object_or_404(Product, pk=item_id)
    #get the number of pictures for the product
    if product.number_of_pictures > 0:
    #read each value from the form 
        number_of_products_to_link = product.number_of_pictures
        linked_products = []
        linked_product_images_list = []
        print("This is what you are looking for")
        for i in range(number_of_products_to_link):
            linked_product_details = request.POST.get('linked_product' + str(i))
            print(linked_product_details)
            split_linked_product_details = linked_product_details.split("|")
            linked_product_id = split_linked_product_details[1]
            linked_product_image = split_linked_product_details[0]
            print(linked_product_image)
            linked_product_type = split_linked_product_details[2]

            if linked_product_images_list != []:
                linked_product_images_list.append(linked_product_image)
            else:
                linked_product_images_list.insert(0, linked_product_image)
            
                
            
            if linked_product_id == "No id":
                linked_products.append(['This is causing the calendars an issue'])
                
            
            # Put in an elif about being an upload and deal with it that way.
            elif linked_product_type == 'upload':
                print('upload function reached')
                linked_product_sku = str(uuid.uuid4())
                linked_product = get_object_or_404(Image_upload, pk=linked_product_id)
                linked_products.append([linked_product_id, linked_product_sku, linked_product.title, linked_product_type])
                
            else:
                linked_product = get_object_or_404(Product, pk=linked_product_id)
                # There are going to be issues with upload your own photos here
                linked_products.append([linked_product_id, linked_product.sku, linked_product.name, linked_product_type])
                


    # appending the items to the basket

    if basket != {}:
        for item in basket['items']:
            basket_item_id = basket_item_id + 1

        matching_items = []
        if linked_products[0] == "Not linked":
            print("nothing to link reached")
            for item in basket['items']:
                # If the ID is in and the the digi-download is on OR off and matches it goes through here. 
                if item_id == item['item_id'] and digital_download == item['digital_download']:
                    print("We have a match")
                    matching_items.append(item)
        else:
            print("this product is linked to a photo")
            for item in basket['items']:
                if item_id == item['item_id'] and linked_products == item['linked_products']:
                    matching_items.append(item)
        if matching_items:
            print("matching items exist")
            if matching_items[0]['item_id'] == item_id:
                matching_items[0]['quantity'] += quantity
        else:
            basket['items'].append({
                'basket_item_id': basket_item_id,
                'item_id': item_id,
                'digital_download': digital_download,
                'quantity': quantity,
                'linked_products': linked_products,
                'linked_product_images_list': linked_product_images_list
            })
    else:
        basket['items'] = []
        request.session['basket_item_id'] = 1
        basket['items'].append({
            'basket_item_id': 1,
            'item_id': item_id,
            'digital_download': digital_download,
            'quantity': quantity,
            'linked_products': linked_products,
            'linked_product_images_list': linked_product_images_list
        })

    redirect_url = request.POST.get('redirect_url')
    request.session['basket'] = basket
    
    print(basket)
    return redirect(redirect_url)

def edit_basket(request):
    basket = request.session.get('basket', {})
    updated_quantity = request.POST.get('basket_quantity')
    updated_delivery = request.POST.get('basket_digital_download')
    print("digital download " + updated_delivery)
    updated_item_id = request.POST.get('basket_item_id')
    
    print("important!" + str(updated_item_id))
    item_number = -1
    for item in basket['items']:
        item_number = item_number + 1
        print("basket item " + str(item['basket_item_id']))
        print(item)
        if int(updated_item_id) == item['basket_item_id']:
            print("match found")
            if int(updated_quantity) == 0:
                print("needs deleting.")
                del basket['items'][item_number]
            else:
                item['quantity'] = int(updated_quantity)
                if updated_delivery == "True":
                    item['digital_download'] = True
                else:
                    item['digital_download'] = None
        else:
            print("else")
                
    request.session['basket'] = basket
    return redirect('view_basket')


def delete_basket_item(request, basket_item_id):
    print("delete function reached")
    basket = request.session.get('basket', {})
    basket_item_id = int(basket_item_id)
    print("basket id from url" + str(basket_item_id))
    print("basket id from url type" + str(type(basket_item_id)))
    item_number = -1
    for item in basket['items']:
        item_number = item_number + 1
        print(item['basket_item_id'])
        print("from session basket id " + str(type(item['basket_item_id'])))
        if item['basket_item_id'] == basket_item_id:
            del basket['items'][item_number]
            request.session['basket'] = basket
    return redirect('view_basket')

def empty_basket(request):
    basket = request.session.get('basket', {})
    del basket['items']
    request.session['basket'] = basket
    return redirect('view_basket')
