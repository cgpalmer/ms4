from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product

# Create your views here.


def view_basket(request):
    # Returning the user's basket
    return render(request, 'basket/basket.html')

def add_to_basket(request, item_id):
    """ Add a quantity of the chosen product to the shopping bag """
    quantity = int(request.POST.get('quantity'))
    # change digital download to a boolean value
    digital_download = request.POST.get('digital_download')
    
    #find the product.
    #find how many pictures there should be.
    # create loop to fetch information for that amount of pictures
    # create list of photos linked to that item

    # This is finding out how many photos need to be linked with the item. 
    product = get_object_or_404(Product, pk=item_id)
    number_of_products_to_link = product.number_of_pictures
    print("number of products " + str(number_of_products_to_link))
    list_of_pictures_to_link_to_a_product = []
    linked_product_details = request.POST.get('linked_product')
    print("These are the linked product details")
    print(linked_product_details)
    print("These are the details split")
    split_linked_product_details = linked_product_details.split("|")
    print(split_linked_product_details)
    print("This is the linked product id")
    linked_product_id = split_linked_product_details[1]
    print(linked_product_id)




    # Once it knows how many it will loop through and get the product from each field sent through the form. 
    # for i in range(number_of_products_to_link):
    #     linked_product_form_id = 'linked_product'+str(i)
    #     linked_product_image = request.POST.get('linked_product')
    #     linked_product_image = get_object_or_404(Product, image_url_mobile=linked_product_image)
    #     if linked_product_image != "Not linked":
    #         linked_product_image = get_object_or_404(Product, image_url_mobile=linked_product_image)
    #         linked_product_name = linked_product_image.name
    #         linked_product_sku = linked_product_image.sku
    #         linked_product_image_path = linked_product_image.image_url_mobile
    #         linked_product_id = linked_product_image.id
    #         list_of_pictures_to_link_to_a_product.append(linked_product_name)
    #         list_of_pictures_to_link_to_a_product.append(linked_product_sku)
    #         list_of_pictures_to_link_to_a_product.append(linked_product_image_path)
    #         list_of_pictures_to_link_to_a_product.append(linked_product_id)

        

    # print("Item ID follows")
    # print(item_id)
    # print(type(item_id))
    # basket = request.session.get('basket', {})
    # print("this is the test from the bag so far")
    # print(basket)
    # if basket != {}:
    #     print("bag exists")
    #     matching_items = []

    #     for item in basket['items']:
    #         print(item)
    #         if linked_product_image == "Not linked":
    #         # If the ID is in and the the digi-download is on OR off and matches it goes through here. 
    #             if item_id == item['item_id'] and digital_download == item['digital_download']:
    #                 print("We have a match")
    #                 matching_items.append(item)
    #         else:
    #             print("this product is linked to a photo")
    #             if item_id == item['item_id'] and linked_product_image == item['linked_product_image']:
    #                 matching_items.append(item)
    #     if matching_items:
    #         print("matching items exist")
    #         if matching_items[0]['item_id'] == item_id:
    #             matching_items[0]['quantity'] += quantity
    #     else:
    #         print("bag exists but no matching item")
    #         if linked_product_image == "Not linked":
    #             basket['items'].append({
    #                         'item_id': item_id,
    #                         'digital_download': digital_download,
    #                         'quantity': quantity,
    #                         'linked_product_id': linked_product_id,
    #                 })
                     
    #         else:
    #             basket['items'].append({
    #                         'item_id': item_id,
    #                         'digital_download': digital_download,
    #                         'quantity': quantity,
    #                          'linked_product_id': linked_product_id,
                             
    #                 })
    #             # loop through the id's and append them these values to them
    #             for pic in linked_product_id:
    #                 basket['items'].append({
    #                     'linked_product_image': linked_product_image_path,
    #                     'linked_product_name': linked_product_name,
    #                     'linked_product_sku': linked_product_sku,
    #                 })
    # else:
    #     print("bag doesnt exist yet.")
    #     basket['items'] = []
    #     if linked_product_image == "Not linked":
    #         basket['items'].append({
    #                     'item_id': item_id,
    #                     'digital_download': digital_download,
    #                     'quantity': quantity,
    #                      'linked_product_id': linked_product_id,
    #             })
    #     else:
    #         basket['items'].append({
    #                     'item_id': item_id,
    #                     'digital_download': digital_download,
    #                     'quantity': quantity,
    #                     'linked_product_id': linked_product_id,
    #                     'linked_product_image': linked_product_image_path,
    #                     'linked_product_name': linked_product_name,
    #                     'linked_product_sku': linked_product_sku,
    #             })
            
    redirect_url = request.POST.get('redirect_url')
    # request.session['basket'] = basket
    # print(basket)
    return redirect(redirect_url)
