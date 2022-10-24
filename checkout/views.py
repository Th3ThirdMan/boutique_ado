from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LwYeUBJDRb5nFZWEp5LKTPrlXKmMXx2qFttw6dIpChONXPKYrrJnmSc273wi4TKGCShBW8vzm3zATxfwbFePf9a00v69wQR6P'
    }

    return render(request, template, context)
