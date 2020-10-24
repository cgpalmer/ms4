from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Blog
from products.models import Product
# Create your views here.
''' A view to show the blog associated with the product.'''


def blog_info(request):
    # Returning the index page

    blogs = Blog.objects.all()
    query = None
    feedback = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            print("this is the query below")
            print(query)
            queries = Q(title__icontains=query) | Q(location__icontains=query)
            blogs = blogs.filter(queries)
            number_of_results_from_search = blogs.count()
            print(type(number_of_results_from_search))
            print(number_of_results_from_search)
            if number_of_results_from_search == 0:
                print("reached")
                feedback = "You didn't find anything"
                blogs = Blog.objects.all()
            elif not query:
                print("reached")
                feedback = "You didn't search anything"
            else:
                feedback = None

    context = {
        'blogs': blogs,
        'search_term': query,
        'feedback': feedback,
    }
    return render(request, 'blog/blog.html', context)


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    product = get_object_or_404(Product, sku=blog.sku)
    context = {
        'blog': blog,
        'product': product,
    }
    return render(request, 'blog/blog_detail.html', context)

def blog_detail_from_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    blog = get_object_or_404(Blog, sku=product.sku)

    context = {
        'blog': blog,
        'product': product,
    }
    return render(request, 'blog/blog_detail.html', context)