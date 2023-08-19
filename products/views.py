from django.shortcuts import render
from .models import Product

def all_products(request):
    """ A view to show all products, including sorting and search queries"""
    products = Product.objects.all()  # Use 'products' with lowercase 'p'

    context = {
        'products': products,  # Use 'products' here as well
    }

    return render(request, 'products/products.html', context)
