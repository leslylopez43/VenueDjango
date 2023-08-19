from django.shortcuts import render, redirect, reverse,  get_object_or_404
from django.contrib import messages
from .models import Product
from django.db.models import Q

def all_products(request):
    """ A view to show all products, including sorting and search queries"""

    products = Product.objects.all()  # Use 'products' with lowercase 'p'
    query = None


    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't any search criteria! ")
                return redirect(reverse ('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries) 

    context = {
        'products': products,  # Use 'products' here as well
        'search_term': query,
    }

    return render(request, 'products/products.html', context)

def venue_detail(request, venue_id):
    """ A view to show all venues, including venue detais"""
    products = get_object_or_404 (Product, pk=venue_id)  # Use 'products' with lowercase 'p'

    context = {
        'products': products,  # Use 'products' here as well
    }

    return render(request, 'products/venue_detail.html', context)