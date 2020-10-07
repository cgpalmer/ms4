from django.shortcuts import render
from .models import Blog
# Create your views here.
''' A view to show the blog associated with the product.'''


def blog_info(request):
    # Returning the index page

    blogs = Blog.objects.all

    context = {
        'blogs': blogs
    }
    return render(request, 'blog/blog.html', context)
