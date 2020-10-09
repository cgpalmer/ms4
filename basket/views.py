from django.shortcuts import render

# Create your views here.


def view_basket(request):
    # Returning the user's basket
    return render(request, 'basket/basket.html')
