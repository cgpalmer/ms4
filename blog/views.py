from django.shortcuts import render
from .models import Blog, Product
# Create your views here.
''' A view to show the blog associated with the product.'''


def blog_info(request):
    # Returning the index page

    blogs = Blog.objects.all
    products = Product.objects.all

    context = {
        'blogs': blogs,
        'products': products
    }
    return render(request, 'blog/blog.html', context)
