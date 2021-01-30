from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import UserProfile, ContentReadyToDownload, Image_upload
from products.models import Product, Category
from checkout.models import Linked_Product
from .forms import UserProfileForm, Image_uploadForm
from checkout.models import Order
from reviews.models import Review
from django.contrib.auth.decorators import login_required
import datetime

''' Boutique Ado - Code Institute - helped me set up the profile
part of the functions. I took that base and created the rest of the
functions around them.
'''


# @login_required
def admin_profile(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    orders = Order.objects.order_by("-date")[:5]

    context = {
        'products': products,
        'categories': categories,
        'orders': orders,
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
    image_form = Image_uploadForm

    # Making digital purchase available for download
    digital_downloads_user = ContentReadyToDownload.objects.filter(user=request.user).exclude(
                            number_of_times_downloaded=True)
    digital_previous_downloads_user = ContentReadyToDownload.objects.filter(user=request.user).exclude(
                                      number_of_times_downloaded=False)

    # Allowing users to upload their photographs
    user_photos = Image_upload.objects.filter(user=request.user)

    user_reviews = Review.objects.filter(user=request.user)

    template = 'profiles/profiles.html'
    context = {
        'current_user': profile,
        'form': form,
        'image_upload_form': image_form,
        'orders': orders,
        'on_profile_page': True,
        'user_photos': user_photos,
        'digital_downloads_user': digital_downloads_user,
        'digital_previous_downloads_user': digital_previous_downloads_user,
        'review': user_reviews,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    linked_product = Linked_Product.objects.filter(order_id=order.id).exclude(linked_product='Not linked').exclude(
                     linked_product='Not available')
    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
        'linked_product': linked_product
    }

    return render(request, template, context)


# This function keeps a copy of any item and it's user, that has been marked for digital download.
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
    user_photo = get_object_or_404(Image_upload, pk=photo_id)
    user_photo.delete()
    messages.success(request, 'Photo successfully deleted')
    return redirect(reverse('profile'))


# @login_required
def image_upload(request, product_id):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = Image_uploadForm(request.POST, request.FILES)
        if form.is_valid():
            user = get_object_or_404(UserProfile, user=request.user)
            title = form.cleaned_data.get("title")
            image = form.cleaned_data.get("image")
            Image_upload.objects.create(title=title, user=user, image=image)
            messages.success(request, 'Image uploaded! Find it in the dropdown menu or on your profile page.')
            return redirect(reverse('product_detail', args=[product_id]))
        else:
            messages.error(request, 'Something went wrong. Please try again.')
    return redirect(reverse('product_detail', args=[product_id]))


@login_required
def image_upload_from_profile(request):
    if request.method == 'POST':
        form = Image_uploadForm(request.POST, request.FILES)
        if form.is_valid():
            user = get_object_or_404(UserProfile, user=request.user)
            title = form.cleaned_data.get("title")
            image = form.cleaned_data.get("image")
            Image_upload.objects.create(title=title, user=user, image=image)
            messages.success(request, 'Image uploaded! Find it in the dropdown menu or on your profile page.')
            return redirect(reverse('profile'))
        else:
            messages.error(request, 'Something went wrong. Please try again.')
    return redirect(reverse('profile'))
