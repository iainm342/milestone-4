from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get("bag", {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse("products"))

    order_form = OrderForm()
    template = "checkout/checkout.html"
    context = {
        "order_form": order_form,
        "stripe_public_key": "pk_test_51IaIRaFW2rFBZfbSkvjQmVopl7MOaKwBZLxG71LEE5PTekdN2c84ncWqFsUoG5SeQHpjCPi1VNBEaHWHvOl0OfKF00YZcF3Ekh",
        "client_secret": "test_client_secret",
    }

    return render(request, template, context)
