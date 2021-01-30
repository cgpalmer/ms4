from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Special
from profiles.models import UserProfile, Image_upload
from django.db.models.functions import Lower
from reviews.models import Review
from .forms import ProductForm
from profiles.forms import Image_uploadForm
from django.contrib.auth.decorators import login_required


def photo_products(request):
    products = Product.objects.filter(product_type="photo")
    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)


def container_products(request):
    products = Product.objects.filter(product_type="container")
    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)


# A view to show all the products and somewhere to search and sort by.
def all_products(request):
    # Returning the products page
    products = Product.objects.all()
    query = None
    categories = None
    special_offer = None
    sort = None
    direction = None

    # Getting search queries from the URL
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
    if request.GET:
        if 'special_offer' in request.GET:
            special_offer = request.GET['special_offer'].split(',')
            if special_offer == ['no_offer']:
                products = products.exclude(special_offer__name__in=special_offer)
            else:
                products = products.filter(special_offer__name__in=special_offer)
            special_offer = Special.objects.filter(name__in=special_offer)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria.")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query) | Q(
                friendly_name__icontains=query) | Q(sku__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'special_offer': special_offer
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    # Returning the details of a specific product.
    product = get_object_or_404(Product, pk=product_id)
    linked_product = Product.objects.filter(product_type="photo")
    user_photos = Image_upload.objects.filter(user=request.user)
    review = Review.objects.filter(product=product_id)

    # Querying the type of product
    if product.product_type == "photo":
        product_type_for_linking = "photo"
    else:
        product_type_for_linking = "container"

    form = Image_uploadForm()

    number_of_pictures = product.number_of_pictures
    number_of_pictures_loop = []
    for n in range(number_of_pictures):
        number_of_pictures_loop.append(n)

    context = {
        'product': product,
        'review': review,
        'linked_product': linked_product,
        'product_type_for_linking': product_type_for_linking,
        'form': form,
        'user_photos': user_photos,
        'number_of_pictures_loop': number_of_pictures_loop
    }
    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Retrieving the product, calculating the price and updating the discount price.
            sku = form.cleaned_data.get("sku")
            retrieve_product = get_object_or_404(Product, sku=sku)
            product_price = retrieve_product.price
            product_discount = 1 - retrieve_product.special_offer.discounts
            discount_price = product_price * product_discount
            retrieve_product.discount_price = discount_price
            retrieve_product.save()
            return redirect(reverse('admin_profile_page'))
        else:
            messages.error(
                request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            sku = form.cleaned_data.get("sku")
            retrieve_product = get_object_or_404(Product, sku=sku)
            product_price = retrieve_product.price
            product_discount = 1 - retrieve_product.special_offer.discounts
            discount_price = product_price * product_discount
            retrieve_product.discount_price = discount_price
            retrieve_product.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('admin_profile_page'))
        else:
            messages.error(
                request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }
    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('admin_profile_page'))
