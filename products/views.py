from django.shortcuts import render, get_object_or_404
from .models import Product

def all_products(request):
    """ A view to show all products, including sorting and search queries"""
    products = Product.objects.all()  # Use 'products' with lowercase 'p'

    context = {
        'products': products,  # Use 'products' here as well
    }

    return render(request, 'products/products.html', context)

def venue_detail(request, venue_id):
    """ A view to show all venues, including venue detais"""
    products = get_object_or_404 (Product, pk=venue_id)  # Use 'products' with lowercase 'p'

    context = {
        'products': products,  # Use 'products' here as well
    }

    return render(request, 'products/venue_detail.html', context)