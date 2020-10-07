from django.shortcuts import render
from .models import Product

# Create your views here.
''' A view to show all the products and somewhere to search and sort by.'''

def all_products(request):
    # Returning the index page

    products = Product.objects.all

    context = {
        'products': products
    }
    return render(request, 'products/products.html', context)
