from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import UserProfile, ContentReadyToDownload
from blog.models import Blog
from products.models import Image_upload, Product, Category
from .forms import UserProfileForm
from reviews.forms import ReviewForm
from checkout.models import Order
from reviews.models import Review
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime


@login_required
def admin_profile(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    orders = Order.objects.order_by("-date")[:5]
    blogs = Blog.objects.all()
    context = {
        'products': products,
        'categories': categories,
        'orders': orders,
        'blogs': blogs
    }
    return render(request, 'profiles/admin_profile_page.html', context)

@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    # Loading all blogs

    blogs = Blog.objects.all()

    # Downloading digital content
    digital_downloads_user = ContentReadyToDownload.objects.filter(user=request.user)
    user_photos = Image_upload.objects.filter(user=request.user)
   
    user_reviews = Review.objects.filter(user=request.user)


    template = 'profiles/profiles.html'
    context = {
        'current_user': profile,
        'form': form,
        'orders': orders,
        'on_profile_page': True,
        'user_photos': user_photos,
        'digital_downloads_user': digital_downloads_user,
        'review': user_reviews,
        
    }

    return render(request, template, context)

def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)



def counting_downloads(request, download_id):
    if request.method == "POST":
        download_file = get_object_or_404(ContentReadyToDownload, pk=download_id)
        download_file.number_of_times_downloaded = True
        download_file.date = datetime.datetime.now()
        download_file.save()    


        template = "profiles/download_ready.html"
        context = {
            'download_file': download_file
        }
        return render(request, template, context)
    else:
        return render(request, 'home/index.html')

def delete_user_photo(request, photo_id):
    # Use a filter here for user photos only
    user_photo = get_object_or_404(Image_upload, pk=photo_id)
    user_photo.delete()
    return redirect(reverse('profile'))


