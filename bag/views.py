from django.shortcuts import render, redirect

def view_bag(request):
    """A view that renders the bag content page"""
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """Add a quantity of the specific product to the shopping bag"""
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']  # Fixed the variable name here
    bag = request.session.get('bag', {})

    if size:
        if item_id in bag.keys():  # Corrected the typo "bag.key()" to "bag.keys()"
            if size in bag[item_id]['items_by_size'].keys():  # Corrected "esle" to "else"
                bag[item_id]['items_by_size'][size] += quantity  # Fixed capitalization of "Quantity"
            else: 
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in bag:
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
