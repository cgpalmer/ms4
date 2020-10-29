from django.shortcuts import render, reverse, redirect
from .forms import ReviewForm
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
