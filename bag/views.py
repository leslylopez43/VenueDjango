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
        bag_items.append({
            'product': product,
            'quantity': quantity,
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
    size = request.POST.get('product_size')
    bag = request.session.get('bag', {})

    if size:
        # Adjust by size
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request,
                             (f'Updated size {size.upper()} '
                              f'{product.name} quantity to '
                              f'{bag[item_id]["items_by_size"][size]}'))
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request,
                             (f'Removed size {size.upper()} '
                              f'{product.name} from your bag'))
    else:
        # Adjust without size
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request,
                             (f'Updated {product.name} '
                              f'quantity to {bag[item_id]}'))
        else:
            bag.pop(item_id)
            messages.success(request,
                             (f'Removed {product.name} '
                              f'from your bag'))

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))



def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = request.POST.get('product_size')
        bag = request.session.get('bag', {})

        if size:
            # Remove by size
            if item_id in bag and 'items_by_size' in bag[item_id] and size in bag[item_id]['items_by_size']:
                del bag[item_id]['items_by_size'][size]
                if not bag[item_id]['items_by_size']:
                    del bag[item_id]['items_by_size']
                    if not bag[item_id]:  # Remove the entire item if no sizes left
                        del bag[item_id]
                messages.success(request,
                                 (f'Removed size {size.upper()} '
                                  f'{product.name} from your bag'))
            else:
                messages.error(request, f"{product.name} not found in your bag")
        else:
            # Remove without size
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