from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import messages
from products.models import Product


# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """
    bag = request.session.get('bag', {})
    bag_items = []

    for item_id, quantity in bag.items():
        product = Product.objects.get(id=item_id)  # Fetch product from DB
        bag_items.append({
            'product': product,
            'quantity': quantity,
        })

    print(bag_items)  # Debugging line to check if items are being passed

    total = sum(item['product'].price * item['quantity'] for item in bag_items)
    delivery = 10.00  # Example, replace with your actual delivery calculation
    grand_total = float(total) + delivery
    free_delivery_delta = max(0, 50 - total)  # Assuming free delivery for orders over $50

    return render(request, 'bag/bag.html', {
        'bag_items': bag_items,
        'total': total,
        'delivery': delivery,
        'grand_total': grand_total,
        'free_delivery_delta': free_delivery_delta
    })



def add_to_bag(request, item_id):
    """ Add a quantity of a specific product """

    if not item_id:
        return HttpResponse('Item ID is missing', status=400)
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url', '/')
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
    """Adjust the quantity of a specified product to the specified amount"""
    product = get_object_or_404(Product, pk=item_id)

    # Get the quantity from the form and validate
    quantity = request.POST.get('quantity')
    if quantity is None or not quantity.isdigit() or int(quantity) < 1:
        messages.error(request, f"Invalid quantity for {product.name}.")
        return redirect(reverse('view_bag'))

    quantity = int(quantity)  # Convert to integer after validation
    
    size = request.POST.get('product_size', None)  # Get size if available
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            # Update size-specific quantity
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
        else:
            # Remove size if quantity is 0
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:  # Remove product if no sizes left
                bag.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} of {product.name} from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity  # Update the main product quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)  # Remove the item if quantity is 0
            messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))



def remove_from_bag(request, item_id):
    """Remove a specific product or a size of a product from the bag"""
    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})

        if item_id in bag:
            if 'product_size' in request.POST:  # Removing a specific size
                size = request.POST['product_size']
                if size in bag[item_id]['items_by_size']:
                    del bag[item_id]['items_by_size'][size]
                    if not bag[item_id]['items_by_size']:  # Remove item if no sizes left
                        del bag[item_id]
                    messages.success(request, f'Removed size {size.upper()} of {product.name} from your bag')
                else:
                    messages.error(request, f"Size {size.upper()} not found for {product.name} in your bag.")
            else:  # Removing the entire product
                del bag[item_id]
                messages.success(request, f'Removed {product.name} from your bag')

            request.session['bag'] = bag
        else:
            messages.error(request, f'{product.name} is not in your bag.')
        
        return redirect(reverse('view_bag'))

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

