from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
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


def review_history(request):
    # filter this to the user at a later time.
    review = Review.objects.all()
    template = 'profiles/edit_reviews.html'
    context = {
        'review': review,
    }
    return render(request, template, context)


def edit_review(request, review_id):
    review = get_object_or_404(request, pk=review_id)
    form = ReviewForm(instance=review)
  
    template = 'profiles/edit_reviews.html'
    context = {
        'review': review,
        'form': form,
    }

    return render(request, template, context)

