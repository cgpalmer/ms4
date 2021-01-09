from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Image_upload, Special, UserProfile
from blog.models import Blog
from reviews.models import Review
from .forms import ProductForm, Image_uploadForm


# Create your views here.
''' A view to show all the products and somewhere to search and sort by.'''

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

def all_products(request):
    # Returning the products page

    products = Product.objects.all()
    query = None
    categories = None
    special_offer = None
    sort = None
    direction = None

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
            print(special_offer)
            if special_offer == ['no_offer']:
                print("-------------------------------")
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
                friendly_name__icontains=query)
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
    print("this is the product id")
    print(product_id)
    product = get_object_or_404(Product, pk=product_id)
    print(product)
    print(product.linked_to_blog)
    linked_product = Product.objects.filter(product_type="photo")
    user_photos = Image_upload.objects.filter(user=request.user)

    # change to id
    if product.linked_to_blog == True:
        print("blog exists")
        try:
            blog = get_object_or_404(Blog, sku=product.sku)
           
        except Exception as e:
            e = None
            print(e)
            blog = e
        
    else:
        blog = None
        
    review = Review.objects.filter(product=product_id)

    if product.product_type == "photo":
        product_type_for_linking = "photo"
    else:
        product_type_for_linking = "container"
    form = Image_uploadForm()

    number_of_pictures = product.number_of_pictures
    print("number of pics is" + str(number_of_pictures))
    number_of_pictures_loop = []
    for n in range(number_of_pictures):
        number_of_pictures_loop.append(n)
        print(number_of_pictures_loop)

    context = {
        'product': product,
        'blog': blog,
        'review': review,
        'linked_product': linked_product,
        'product_type_for_linking': product_type_for_linking,
        'form': form,
        'user_photos': user_photos,
        'number_of_pictures_loop': number_of_pictures_loop

    }
    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            # question this
            product = form.save()
            # Retrieving the product, calculating the price and updating the discount price.
            sku = form.cleaned_data.get("sku")
            retrieve_product = get_object_or_404(Product, sku=sku)
            product_price = retrieve_product.price
            
            
            product_discount = 1 - retrieve_product.special_offer.discounts
            discount_price = product_price * product_discount
            retrieve_product.discount_price = discount_price
            print(product_price)
            print(product_discount)
            print(discount_price)
            print("end of the price stuff")

            # # http://www.learningaboutelectronics.com/Articles/How-to-retrieve-data-from-a-Django-form-Python.php#:~:text=Basically%20to%20extract%20data%20from,this%20function%20as%20a%20parameter.
            # # Filling out the blog information
            # sku = form.cleaned_data.get("sku")
            # title = form.cleaned_data.get("name")
            # Blog.objects.create(title=title, sku=sku)
            # retrieve_blog = get_object_or_404(Blog, sku=sku)
            # retrieve_blog.product = retrieve_product
            # retrieve_blog.image_mobile_url = retrieve_product.image_url_mobile
            # retrieve_blog.image_desktop_url = retrieve_product.image_url_mobile
            retrieve_product.save()
            # retrieve_blog.save()
            return redirect(reverse('products'))
        else:
            messages.error(
                request, 'Failed to add product. Please ensure the form is valid.')
            # deal with this
            return redirect(reverse('products'))
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


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


def delete_product(request, product_id):
    """ Delete a product from the store """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    blog = get_object_or_404(Blog, product=product.id)
    print(blog)
    blog.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))

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
    return redirect(reverse('product_detail', args=[product_id]))
