from django.shortcuts import render, get_object_or_404, reverse, redirect
from .forms import ReviewForm
from django.contrib import messages

# Create your views here.

def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save()
            return redirect(reverse('products'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')  
            print("you've gone past the error messages.")
            return redirect(reverse('add_review'))
    else:
        form = ReviewForm()
        template = "reviews/add_review.html"

        context = {
                'form': form
        }
        return render(request, template, context)
