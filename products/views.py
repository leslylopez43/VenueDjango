from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm

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

    current_sorting = f'Sort by {sort} ({direction})'

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
        'venue_id': venue_id,
    }
    return render(request, 'products/venue_detail.html', {'product': product})


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('venue_detail', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to add product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,

    }

    return render(request, template, context)


@login_required
def edit_product(request, venue_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=venue_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Venue!')
            return redirect(reverse('edit_product', args=[venue_id]))
        else:
            messages.error(request, 'Failed to update venue. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
        'venue_id': venue_id,
    }

    return render(request, template, context)


@login_required
def delete_product(request, venue_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=venue_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect('products')