from django.shortcuts import render, reverse, redirect, get_object_or_404
from .forms import ReviewForm
from .models import Review
from django.contrib import messages

# Create your views here.


def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save()
            messages.success(request, 'Review added.')
            print("Review added.")
            return redirect(reverse('products'))
        else:
            messages.error(request, "'Failed to add product.")
            print("you've gone past the error messages.")
            return redirect(reverse('add_review'))
    else:
        form = ReviewForm()
        template = "reviews/add_review.html"

        context = {
                'form': form
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

def edit_review(request, r_id):
    """ Edit a product in the store """
    review = get_object_or_404(Review, pk=r_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('products'))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ReviewForm(instance=review)
        messages.info(request, 'something')

        template = 'reviews/edit_reviews.html'
        context = {
            'form': form,
            'r': review,
        }

        return render(request, template, context)