from django.shortcuts import render, reverse, redirect, get_object_or_404
from .forms import ReviewForm
from .models import Review
from products.models import Product
from django.contrib import messages

# Create your views here.


def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            review_rating = form.cleaned_data.get("review_rating")
            product = form.cleaned_data.get("product")
            review_content = form.cleaned_data.get("review_content")

            Review.objects.create(user=user, review_rating=review_rating, product=product, review_content=review_content)

            # retrieve data from current product
            product_name = form.cleaned_data.get("product")
            print(product_name)
            # change this t product id.
            retrieve_product = get_object_or_404(Product, name=product_name)
            print(retrieve_product.name)
            number_of_ratings = retrieve_product.number_of_ratings
            ratings_total = retrieve_product.rating_total
            print(ratings_total)

            # retrieving data from the form 
            new_rating_score = form.cleaned_data.get("review_rating")
            print("new rating score")
            print(new_rating_score)

            # Average rating calculations
            # Adding up the total score of all the reviews
            retrieve_product.rating_total = ratings_total + new_rating_score
            print("ratings total")
            print(retrieve_product.rating_total)

            # Adding 1 to the amount of reviews under the product
            retrieve_product.number_of_ratings = number_of_ratings + 1
            print("How many reviews there are")
            print(retrieve_product.number_of_ratings)

            # Finding the average of the reviews
            retrieve_product.rating = retrieve_product.rating_total / retrieve_product.number_of_ratings
            print("Average rating")
            print(retrieve_product.rating)

            retrieve_product.save()
            
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
    review = Review.objects.filter(user=request.user)
    template = 'reviews/includes/review_history.html'
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

def delete_review(request, r_id):

    # Refactor the retrieving products code because there is unnecessary repetition.
    """ Delete a product from the store """
    # retrieve the review and product to manipulate both
    review = get_object_or_404(Review, pk=r_id)
    product = get_object_or_404(Product, name=review.product)
    old_number_of_ratings = product.number_of_ratings
    old_rating_total = product.rating_total
    old_rating = product.rating

    print(old_number_of_ratings)
    print(old_rating_total)
    print(old_rating)

    # Calculating the new rating scores.
    product.number_of_ratings = product.number_of_ratings - 1
    print("new number of ratings")
    print(product.number_of_ratings)
    print("new product rating total")
    product.rating_total = product.rating_total - review.review_rating
    print(product.rating_total)
    if product.number_of_ratings != 0:
        product.rating = product.rating_total / product.number_of_ratings
        print("product rating new")
        print(product.rating)
    else:
        product.rating = 0
    review.delete()
    product.save()
    messages.success(request, 'Review deleted!')
    return redirect(reverse('products'))
