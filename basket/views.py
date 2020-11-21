from django.shortcuts import render, redirect

# Create your views here.


def view_basket(request):
    # Returning the user's basket
    return render(request, 'basket/basket.html')

def add_to_basket(request, item_id):
    """ Add a quantity of the chosen product to the shopping bag """
    quantity = int(request.POST.get('quantity'))
    # change digital download to a boolean value
    digital_download = request.POST.get('digital_download')
    linked_product = request.POST.get('linked_product')
    print("linked:" + linked_product)
    print("Item ID follows")
    print(item_id)
    print(type(item_id))
    basket = request.session.get('basket', {})
    print("this is the test from the bag so far")
    print(basket)
    if basket != {}:
        print("bag exists")
        matching_items = []

        for item in basket['items']:
            print(item)
            # If the ID is in and the the digi-download is on OR off and matches it goes through here. 
            if item_id == item['item_id'] and digital_download == item['digital_download']:
                print("We have a match")
                matching_items.append(item)
        if matching_items:
            print("matching items exist")
            if matching_items[0]['item_id'] == item_id:
                matching_items[0]['quantity'] += quantity
        else:
            print("bag exists but no matching item")
            basket['items'].append({
                        'item_id': item_id,
                        'digital_download': digital_download,
                        'quantity': quantity,
                        'linked_product': linked_product
                        
                })
    else:
        print("bag doesnt exist yet.")
        basket['items'] = []
        basket['items'].append({
                    'item_id': item_id,
                    'digital_download': digital_download,
                    'quantity': quantity,
                    'linked_product': linked_product
            })
            
    redirect_url = request.POST.get('redirect_url')
    request.session['basket'] = basket
    print(basket)
    return redirect(redirect_url)
