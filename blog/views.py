from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.
''' A view to show the blog associated with the product.'''


def blog_info(request):
    # Returning the index page

    blogs = Blog.objects.all


    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/blog.html', context)


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    context = {
        'blog': blog,
    }
    return render(request, 'blog/blog_detail.html', context)


