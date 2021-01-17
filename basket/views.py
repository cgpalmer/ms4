from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product, Image_upload
from django.contrib import messages

# Create your views here.


def view_basket(request):
    # Returning the user's basket
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    # adding to a basket
    basket = request.session.get('basket', {})
    # When the basket is empty this is set to one. Then one is added each time.
    basket_item_id = request.session.get('basket_item_id')
    print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
    print("basket_item_id")
    print(basket_item_id)
    quantity = int(request.POST.get('quantity'))
    digital_download = request.POST.get('digital_download')
    linked_products = [['Not linked']]
    # item id is passed through as parameter.
    # get the product
    product = get_object_or_404(Product, pk=item_id)
    # get the number of pictures for the product
    if product.number_of_pictures > 0:
        # read each value from the form
        number_of_products_to_link = product.number_of_pictures
        linked_products = []
        linked_product_images_list = []
        for i in range(number_of_products_to_link):
            linked_product_details = request.POST.get('linked_product' + str(i))
            split_linked_product_details = linked_product_details.split("|")
            linked_product_id = split_linked_product_details[1]
            linked_product_image = split_linked_product_details[0]
            linked_product_type = split_linked_product_details[2]
            if linked_product_type == 'upload':
                linked_product_object = get_object_or_404(Image_upload, pk=linked_product_id)
            if linked_product_images_list != []:
                if linked_product_type == "upload":
                    linked_product_image = "/media/" + linked_product_image
                    linked_product_images_list.append(linked_product_image)
                else:
                    linked_product_images_list.append(linked_product_image)
            else:
                if linked_product_type == "upload":
                    linked_product_image = "/media/" + linked_product_image
                    linked_product_images_list.insert(0, linked_product_image)
                else:
                    linked_product_images_list.insert(0, linked_product_image)
            if linked_product_id == "No id":
                if linked_products != []:
                    linked_products.append('Not linked')
                else:
                    linked_products.insert(0, 'Not linked')
            # Put in an elif about being an upload and deal with it that way.
            elif linked_product_type == 'upload':
                if linked_products != []:
                    linked_products.append(str(linked_product_object.sku))
                else:
                    linked_products.insert(0, str(linked_product_object.sku))
            else:
                linked_product = get_object_or_404(Product, pk=linked_product_id)
                # There are going to be issues with upload your own photos here
                if linked_products != []:
                    linked_products.append(linked_product.sku)
                else:
                    linked_products.insert(0, linked_product.sku)
    else:
        linked_products = ['Not available']
        linked_product_images_list = ['Not available']
    # checking to see if any of the linked products has repeated pictures to give the user a warning.
    repeats_found = 'None'
    if product.number_of_pictures > 1:
        for i in range(0, len(linked_products)):
            for j in range(i+1, len(linked_products)):
                if linked_products[i] == linked_products[j]:
                    if linked_products[i] != "Not linked":
                        repeats_found = 'There are repeated pictures in your product.'
    # appending the items to the basket
    if basket != {}:
        print("--------------------------")
        print(basket_item_id)
        basket_item_id