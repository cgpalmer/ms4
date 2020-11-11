from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import UserProfile, ContentReadyToDownload
from .forms import UserProfileForm
from reviews.forms import ReviewForm
from checkout.models import Order
from reviews.models import Review

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
    template = 'profiles/new_profile.html'
    context = {
        'digital_downloads': digital_downloads
    }

    return render(request, template, context)


def add_content_for_download(request, product_id):
    if request.method == 'POST':
        # in future can you use the order number to find any that are a certain type?
        user = request.POST.get('user')
        sku = request.POST.get('sku')
        name = request.POST.get('name')
        # Check what happens in the item line when someone orders two.
        product_file_path = request.POST.get('product_file_path')
        number_of_times_downloaded = 0
        ContentReadyToDownload.objects.create(user=user, sku=sku, name=name, product_file_path=product_file_path, number_of_times_downloaded=number_of_times_downloaded)
        return redirect(reverse('new_profile'))
    else:
        return redirect(reverse('products'))


def counting_downloads(request, download_id):
    if request.method == "POST":
        download_file = get_object_or_404(ContentReadyToDownload, pk=download_id)
        
        template = "profiles/download_finished.html"
        context = {
            'download_file': download_file
        }
        return render(request, template, context)
    else:
        return render(request, 'home/index.html')



