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
    print("Item ID follows")
    print(item_id)
    print(type(item_id))
    test = request.session.get('test', {})
    print("this is the test from the bag so far")
    print(test)
    if test != {}:
        print("bag exists")
        matching_items = []

        for item in test['items']:
            print(item)
            if item_id == item['item_id'] and digital_download == item['digital_download']:
                print("We have a match")
                matching_items.append(item)
        if matching_items:
            print("matching items exist")
            if matching_items[0]['item_id'] == item_id:
                test['items'].append({
                        'item_id': item_id,
                        'digital_download': digital_download,
                        'quantity': quantity
                })
        else:
            print("bag exists but no matching item")
            test['items'].append({
                        'item_id': item_id,
                        'digital_download': digital_download,
                        'quantity': quantity
                })
    else:
        print("bag doesnt exist yet.")
        test['items'] = []
        test['items'].append({
                    'item_id': item_id,
                    'digital_download': digital_download,
                    'quantity': quantity
            })
            

    # print(test)
    # quantity = int(request.POST.get('quantity'))
    # digital_download = None
    # print("quantity")
    # print(quantity)
    # if 'digital_download' in request.POST:
    #     digital_download = request.POST.get('digital_download')
    #     print(digital_download)
    redirect_url = request.POST.get('redirect_url')
    # basket = request.session.get('basket', {})
  
    # if digital_download:
      
    
    #     if item_id in list(basket.keys()):
    #         if digital_download in basket[item_id]['items_by_digital_download'].keys():
    #             basket[item_id]['items_by_digital_download'][digital_download] += quantity
    #         else:
    #             basket[item_id]['items_by_digital_download'][digital_download] = quantity
    #     else:
    #         digital_download[item_id] = {'items_by_digital_download': {digital_download: quantity}}
    # else:
    #     if item_id in list(basket.keys()):
    #         basket[item_id] += quantity
    #     else:
    #         basket[item_id] = quantity

    

    request.session['test'] = test
    # request.session['data'] = data
    # print(basket)
    return redirect(redirect_url)
