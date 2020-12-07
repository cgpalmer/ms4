from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import UserProfile, ContentReadyToDownload
from products.models import Image_upload
from .forms import UserProfileForm
from reviews.forms import ReviewForm
from checkout.models import Order
from reviews.models import Review
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

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

    template = 'profiles/profiles.html'
    context = {
        'current_user': profile,
        'form': form,
        'orders': orders,
        'on_profile_page': True
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

def new_profile(request):
    digital_downloads = ContentReadyToDownload.objects.all()
    user_photos = Image_upload.objects.all()
    digital_downloads_user = ContentReadyToDownload.objects.filter(user=request.user)
    print(digital_downloads_user)
    template = 'profiles/new_profile.html'
    context = {
        'digital_downloads': digital_downloads,
        'user_photos': user_photos,
        'digital_downloads_user': digital_downloads_user
    }

    return render(request, template, context)



def counting_downloads(request, download_id):
    if request.method == "POST":
        download_file = get_object_or_404(ContentReadyToDownload, pk=download_id)
        download_file.number_of_times_downloaded = True
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
    return redirect(reverse('new_profile'))


