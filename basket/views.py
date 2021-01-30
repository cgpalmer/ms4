from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from profiles.models import Image_upload
from django.contrib import messages


# Returning the user's basket
def view_basket(request):
    return render(request, 'basket/basket.html')


''' This add_to_basket function will add a product to the basket. It receive the information from a form,
    store the information in a json and then save the basket.
    It has several feature checks along the way: type of delivery, any linked products?,
    checking for duplicated linked products. Linked products are photographs that can
    be added to a container purchase.'''


def add_to_basket(request, item_id):
    if request.method == 'POST':
        # Requesting basket information
        basket = request.session.get('basket', {})
        basket_item_id = request.session.get('basket_item_id')

        # Retrieving form data
        quantity = int(request.POST.get('quantity'))
        digital_download = request.POST.get('digital_download')
        print("Printing digital download " + str(digital_download))
        print(type(digital_download))
        print(digital_download)
        linked_products = [['Not linked']]  # Default setting
        product = get_object_or_404(Product, pk=item_id)

        # Item id is passed through as parameter to identify the linked product.
        processing_linked_products_images_for_basket_preview(request, item_id)
        linked_product_images_list = processing_linked_products_images_for_basket_preview(request, item_id)

        processing_linked_products_for_checkout_summary(request, item_id)
        linked_products = processing_linked_products_for_checkout_summary(request, item_id)

        checking_for_repeated_linked_images(request, item_id, linked_products)
        repeats_found = checking_for_repeated_linked_images(request, item_id, linked_products)

        if basket != {}:
            for item in basket['items']:
                basket_item_id = basket_item_id + 1

            # This next function decides whether the product already exists in the basket.
            matching_items = []
            if linked_products[0] == "Not available":
                for item in basket['items']:
                    # If the ID is in and the the digi-download is on OR off and matches it goes through here.
                    if item_id == item['item_id'] and digital_download == item['digital_download']:
                        matching_items.append(item)
            else:
                for item in basket['items']:
                    if item_id == item['item_id'] and linked_products == item['linked_products']:
                        matching_items.append(item)

            # This next section will either update an basket item quantity or append a new item.
            if matching_items:
                if matching_items[0]['item_id'] == item_id:
                    matching_items[0]['quantity'] += quantity
            else:
                basket['items'].append({
                    'basket_item_id': basket_item_id,
                    'item_id': item_id,
                    'digital_download': digital_download,
                    'quantity': quantity,
                    'linked_products': linked_products,
                    'linked_product_images_list': linked_product_images_list,
                    'repeats_found': repeats_found
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
                'linked_product_images_list': linked_product_images_list,
                'repeats_found': repeats_found
            })

        redirect_url = request.POST.get('redirect_url')
        request.session['basket'] = basket
        messages.success(request, f"Successfully added '{product.friendly_name}' to your basket.")
    else:
        redirect_url = 'home/index.html'
    return redirect(redirect_url)


def checking_for_repeated_linked_images(request, item_id, linked_products):
    # checking to see if any of the linked products has repeated pictures to give the user a warning.
    product = get_object_or_404(Product, pk=item_id)
    repeats_found = 'None'
    if product.number_of_pictures > 1:
        for i in range(0, len(linked_products)):
            for j in range(i+1, len(linked_products)):
                if linked_products[i] == linked_products[j]:
                    if linked_products[i] != "Not linked":
                        repeats_found = 'There are repeated pictures in your product.'
    return repeats_found


def processing_linked_products_images_for_basket_preview(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    if product.number_of_pictures > 0:
        # read each value from the form
        number_of_products_to_link = product.number_of_pictures
        linked_product_images_list = []

        # Splitting the linked_products meta-data and appending them to the arrays above.
        for i in range(number_of_products_to_link):
            linked_product_details = request.POST.get('linked_product' + str(i))
            split_linked_product_details = linked_product_details.split("|")

            linked_product_image = split_linked_product_details[0]
            linked_product_type = split_linked_product_details[2]

            # This process the different paths needed to display the linked images of each product in basket.
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
    else:
        linked_product_images_list = ['Not available']
    linked_product_images_list = linked_product_images_list
    return linked_product_images_list


def processing_linked_products_for_checkout_summary(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    linked_products = []

    if product.number_of_pictures > 0:
        # read each value from the form
        number_of_products_to_link = product.number_of_pictures

        # Splitting the linked_products meta-data and appending them to the arrays above.
        for i in range(number_of_products_to_link):
            linked_product_details = request.POST.get('linked_product' + str(i))
            split_linked_product_details = linked_product_details.split("|")
            linked_product_id = split_linked_product_details[1]
            linked_product_type = split_linked_product_details[2]

            if linked_product_type == 'upload':
                linked_product_object = get_object_or_404(Image_upload, pk=linked_product_id)

            # This stores the different SKU in an array for the order summary.
            if linked_product_id == "No id":
                if linked_products != []:
                    linked_products.append('Not linked')
                else:
                    linked_products.insert(0, 'Not linked')
            elif linked_product_type == 'upload':
                if linked_products != []:
                    linked_products.append(str(linked_product_object.sku))
                else:
                    linked_products.insert(0, str(linked_product_object.sku))
            else:
                linked_product = get_object_or_404(Product, pk=linked_product_id)
                if linked_products != []:
                    linked_products.append(linked_product.sku)
                else:
                    linked_products.insert(0, linked_product.sku)
    else:
        linked_products = ['Not available']
    linked_products = linked_products
    return linked_products


def edit_basket(request):
    basket = request.session.get('basket', {})
    updated_quantity = request.POST.get('basket_quantity')
    updated_delivery = request.POST.get('basket_digital_download')
    basket_item_id = request.POST.get('basket_item_id')

    # Getting variables to set up editing the linked photos
    product_id = request.POST.get('product_id')
    product = get_object_or_404(Product, pk=product_id)
    item_number = -1
    for item in basket['items']:
        item_number = item_number + 1
        if int(basket_item_id) == item['basket_item_id']:
            # Updating the quantity
            print(item['quantity'])
            if int(updated_quantity) == 0:
                del basket['items'][item_number]
            else:
                item['quantity'] = int(updated_quantity)

            # Updating the digital download if necessary
            if product.digital_download is True:
                if updated_delivery == "True":
                    item['digital_download'] = 'on'
                    item['quantity'] = 1
                    messages.warning(request, "Digital purchases are restricted to a quantity of 1.")
                else:
                    item['digital_download'] = None

            # Checking if editing the basket had changed the linked products
            updated_linked_product_images_list = []
            updated_linked_products = []
            if product.number_of_pictures > 0:
                for i in range(product.number_of_pictures):
                    linked_product_details = request.POST.get('edit-linked-product' + str(i))
                    split_linked_product_details = linked_product_details.split("|")
                    linked_product_id = split_linked_product_details[1]
                    linked_product_image = split_linked_product_details[0]
                    linked_product_type = split_linked_product_details[2]

                    # Changing media paths depending if the user is using their own photo.
                    if linked_product_type == "upload":
                        linked_product_image = "/media/" + linked_product_image
                        updated_linked_product_images_list.append(linked_product_image)
                    else:
                        updated_linked_product_images_list.append(linked_product_image)

                    if linked_product_id == "No id":
                        linked_product = 'Not linked'
                    elif linked_product_type == 'upload':
                        linked_product_object = get_object_or_404(Image_upload, pk=linked_product_id)
                        linked_product = linked_product_object.sku
                    else:
                        linked_product_object = get_object_or_404(Product, pk=linked_product_id)
                        linked_product = linked_product_object.sku

                    if updated_linked_products != []:
                        updated_linked_products.append(linked_product)
                    else:
                        updated_linked_products.insert(0, linked_product)
            else:
                updated_linked_products = ['Not available']
                updated_linked_product_images_list = ['Not available']
            item['linked_products'] = updated_linked_products
            item['linked_product_images_list'] = updated_linked_product_images_list

    request.session['basket'] = basket
    return redirect('view_basket')


def delete_basket_item(request, basket_item_id):
    basket = request.session.get('basket', {})
    basket_item_id = int(basket_item_id)
    item_number = -1
    for item in basket['items']:
        item_number = item_number + 1
        if item['basket_item_id'] == basket_item_id:
            del basket['items'][item_number]
            request.session['basket'] = basket
    return redirect('view_basket')


def empty_basket(request):
    emptyingBasket(request)
    return redirect('view_basket')


def emptyingBasket(request):
    basket = request.session.get('basket', {})
    if basket != {}:
        del basket['items']
        request.session['basket'] = basket
    return basket
