from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import OrderForm
from .models import Product


# Assuming you have a function to calculate the grand total of the shopping bag

def calculate_grand_total(bag):
    grand_total = 0
    for product_id, quantity in bag.items():
        product = Product.objects.get(id=product_id)  # Retrieve product from DB
        grand_total += product.price * quantity
    return grand_total


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect('view_bag')

    order_form = OrderForm()
    grand_total = calculate_grand_total(bag)  # Now calling the function here

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'grand_total': grand_total,  # Pass grand total to the template
    }

    return render(request, template, context)
