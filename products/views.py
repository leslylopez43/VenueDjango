from django.shortcuts import render, redirect, reverse, get_object_or_404  
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category
from django.conf import settings
from .forms import BookingForm 
from django.http import Http404
from django.http import HttpResponse

# Your other import statements and view functions


# Create your views here.

def all_products(request):
    
    """A view to show all products, including sorting and search queries"""

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey =='name':
                sortkey = 'lower_name'
                products =products.annotate(lower_name = Lower('name'))
            if sortkey == 'category': 
               sortkey = 'category__name'

            if 'direction' in request.GET:
                direction =request.GET['direction']
                if direction == 'desc':
                    sortkey = f'{sortkey}'
            products = products.order_by(sortkey)


        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't provide any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'(sort) -- (direction)'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories, 
        'current_sorting' : current_sorting,
    }

    return render(request, 'products/products.html', context)

def venue_detail(request, venue_id):
    """A view to show venue details"""
    product = get_object_or_404(Product, pk=venue_id)  # Rename 'products' to 'product'
    
    try:
        booking_date = request.GET.get('booking_date', 'default_value_if_not_provided')
    except KeyError:
        raise Http404("Booking date not provided in the URL.")
    
    context = {
        'product': product,  # Rename 'products' to 'product' here as well
        'booking_date': booking_date,
    }
    return render(request, 'products/venue_detail.html', {'product': product})


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    # Rest of your view logic...
    return render(request, 'checkout/checkout.html', {'stripe_public_key': stripe_public_key})


# def edit_product(request, product_id):
#     product = get_object_or_404(Product, pk=product_id)
#     # Other view logic, if any
#     return render(request, 'products/venue_detail.html', {'product': product})

# def delete_product(request, product_id):
#     product = get_object_or_404(Product, pk=product_id)
#     # Other view logic, if any
#     return render(request, 'products/venue_detail.html', {'product': product})







