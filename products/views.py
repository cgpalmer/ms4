from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
''' A view to show all the products and somewhere to search and sort by.'''

def all_products(request):
    # Returning the products page

    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    # Returning the details of a specific product.

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)
