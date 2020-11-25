from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product

# Create your views here.


def view_basket(request):
    # Returning the user's basket
    return render(request, 'basket/basket.html')

def add_to_basket(request, item_id):
    # """ Add a quantity of the chosen product to the shopping bag """
    # quantity = int(request.POST.get('quantity'))
    # # change digital download to a boolean value
    # digital_download = request.POST.get('digital_download')
    
    # #find the product.
    # #find how many pictures there should be.
    # # create loop to fetch information for that amount of pictures
    # # create list of photos linked to that item

    # # This is finding out how many photos need to be linked with the item.
    # # product = get_object_or_404(Product, pk=item_id)
    # # if product.number_of_pictures >0:
    # #     number_of_products_to_link = product.number_of_pictures
    # #     list_of_associated_products = {}
        

    # #     # Once it knows how many it will loop through and get the product from each field sent through the form. 
    # #     for i in range(number_of_products_to_link):
    # #         linked_product_details = request.POST.get('linked_product' + str(i))
    # #         split_linked_product_details = linked_product_details.split("|")
    # #         linked_product_id = split_linked_product_details[1]
    # #         linked_product_image = split_linked_product_details[0]
    # #         if linked_product_image != "Not linked":
    # #             linked_product = get_object_or_404(Product, pk=linked_product_id)

    # #             list_of_associated_products[f'linked_product{i}'].append({
    # #                 'linked_product_id': linked_product.id,
    # #                 'linked_product_image': linked_product_image,
    # #                 'linked_product_sku': linked_product.sku,
    # #                 'linked_product_name': linked_product.name
    # #             })
                
    # #         else:
    # #             list_of_associated_products[f'linked_product{i}'] = []
    # #             list_of_associated_products[f'linked_product{i}'].append({
    # #                 'linked_product_id': "Not linked",
    # #                 'linked_product_image': "Not linked",
    # #                 'linked_product_sku': "Not linked",
    # #                 'linked_product_name': "Not linked",
    # #             })
    # # else:
    # #     list_of_associated_products = "No linked photos"
    

    # # print(list_of_associated_products)

    # print("Item ID follows")
    # print(item_id)
    # print(type(item_id))
    # basket = request.session.get('basket', {})
    # print("this is the test from the bag so far")
    # print(basket)
    # list_of_associated_products = "No linked photos"
    # if basket != {}:
    #     print("bag exists")
    #     matching_items = []

    #     for item in basket['items']:
    #         print(item)

    #         product = get_object_or_404(Product, pk=item_id)
    #         if product.number_of_pictures >0:
    #             number_of_products_to_link = product.number_of_pictures
    #             list_of_associated_products = {}
            
    #             for i in range(number_of_products_to_link):
    #                 linked_product_details = request.POST.get('linked_product' + str(i))
    #                 split_linked_product_details = linked_product_details.split("|")
    #                 linked_product_id = split_linked_product_details[1]
    #                 linked_product_image = split_linked_product_details[0]
                    
    #                 if linked_product_image != "Not linked":
    #                     linked_product = get_object_or_404(Product, pk=linked_product_id)
    #                     linked_product = get_object_or_404(Product, pk=linked_product_id)
    #                     list_of_associated_products[f'linked_product{i}'] = []
    #                     list_of_associated_products[f'linked_product{i}'].append({
    #                         'linked_product_id': linked_product.id,
    #                         'linked_product_image': linked_product_image,
    #                         'linked_product_sku': linked_product.sku,
    #                         'linked_product_name': linked_product.name
    #                     })
                       
    #                 else:
    #                     list_of_associated_products[f'linked_product{i}'] = []
    #                     list_of_associated_products[f'linked_product{i}'].append({
    #                         'linked_product_id': "Not linked",
    #                         'linked_product_image': "Not linked",
    #                         'linked_product_sku': "Not linked",
    #                         'linked_product_name': "Not linked",
    #                     })

    #         else:
    #             list_of_associated_products = "No linked photos"
                    

    #         if list_of_associated_products == "No linked photos":
    #         # If the ID is in and the the digi-download is on OR off and matches it goes through here. 
    #             if item_id == item['item_id'] and digital_download == item['digital_download']:
    #                 print("We have a match")
    #                 matching_items.append(item)
    #         else:
    #             print("this product is linked to a photo")
    #             if item_id == item['item_id'] and list_of_associated_products == item['list_of_associated_products']:
    #                 matching_items.append(item)
    #     if matching_items:
    #         print("matching items exist")
    #         if matching_items[0]['item_id'] == item_id:
    #             matching_items[0]['quantity'] += quantity
    #     else:
    #         print("bag exists but no matching item")
    #         # How do you get test to display in context? First, replicate this across all scenarios and maybe
    #         # change test to just the id. You will need to move testy out of the condition blocks.
    #         testy = []
    #         testy.append(linked_product_id)
    #         testy.append(linked_product_image)
    #         testy.append(linked_product.sku)
    #         testy.append(linked_product.name)
    #         basket['items'].append({
    #                 'item_id': item_id,
    #                 'digital_download': digital_download,
    #                 'quantity': quantity,
    #                 'list_of_associated_products': list_of_associated_products,
    #         # })
    #         # basket['items'].append({
    #                 'test': testy
    #             })
            
    # else:
    #     print("bag doesnt exist yet.")
    #     basket['items'] = []
    #     testy = ['testy']
    #     basket['items'].append({
    #         'item_id': item_id,
    #         'digital_download': digital_download,
    #         'quantity': quantity,
    #         'list_of_associated_products': list_of_associated_products,
    #         'test': testy
    #     })




    #adding to a basket
    basket = request.session.get('basket', {})
    quantity = int(request.POST.get('quantity'))
    digital_download = request.POST.get('digital_download')
    print("digi downl " + str(digital_download))
    linked_products = ['Nothing to link']
    # item id is passed through as parameter.
    #get the product
    product = get_object_or_404(Product, pk=item_id)
    #get the number of pictures for the product
    if product.number_of_pictures > 0:
    #read each value from the form 
        number_of_products_to_link = product.number_of_pictures
        linked_products = []
        for i in range(number_of_products_to_link):
            linked_product_details = request.POST.get('linked_product' + str(i))
            split_linked_product_details = linked_product_details.split("|")
            linked_product_id = split_linked_product_details[1]
            linked_product_image = split_linked_product_details[0]
            
            if linked_product_id != "No id":
                linked_product = get_object_or_404(Product, pk=linked_product_id)
                # There are going to be issues with upload your own photos here
                linked_products.append([linked_product_id, linked_product_image, linked_product.sku, linked_product.name])
            else:
                linked_products.append([linked_product_id, linked_product_image, 'no sku', 'no name'])


    # appending the items to the basket

    if basket != {}:
        matching_items = []
        if linked_products[0] == "Nothing to link":
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
                'item_id': item_id,
                'digital_download': digital_download,
                'quantity': quantity,
                'linked_products': linked_products
            })
    else:
        basket['items'] = []
        basket['items'].append({
            'item_id': item_id,
            'digital_download': digital_download,
            'quantity': quantity,
            'linked_products': linked_products
        })

    redirect_url = request.POST.get('redirect_url')
    request.session['basket'] = basket
    print(basket)
    return redirect(redirect_url)
