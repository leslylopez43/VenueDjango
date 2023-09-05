from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """ A view that renders the bag contents page """
    bag_items = []  # Initialize an empty list to hold bag items

    # Retrieve bag items from the session and create a list of products
    bag = request.session.get('bag', {})
    for item_id, quantity in bag.items():
        product = Product.objects.get(pk=item_id)
        # Include 'item_id' in the bag item dictionary
        bag_items.append({
            'product': product,
            'quantity': quantity,
            'item_id': item_id,  # Include the 'item_id' attribute
        })

    return render(request, 'bag/bag.html', {'bag_items': bag_items})

    


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    
    bag = request.session.get('bag', {})

    if item_id in bag:
        bag[item_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)



def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product in the bag"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    # Adjust the quantity for the item
    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        # Remove the item if quantity is zero or negative
        bag.pop(item_id, None)
        messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})

        # Remove the item from the bag
        if item_id in bag:
            del bag[item_id]
            messages.success(request, f'Removed {product.name} from your bag')
        else:
            messages.error(request, f"{product.name} not found in your bag")

        request.session['bag'] = bag
        return JsonResponse({'status': 'success'})

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return JsonResponse({'status': 'error'}, status=500)


