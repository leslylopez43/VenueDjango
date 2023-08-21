from django.shortcuts import render, redirect

def view_bag(request):
    """A view that renders the bag content page"""
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """Add a quantity of the specific product to the shopping bag"""
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    
    bag = request.session.get('bag', {})  # Corrected the typo here
    
    if item_id in bag:
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    
    
    return redirect(redirect_url)
