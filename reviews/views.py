from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .models import Review
from .forms import ReviewForm
from products.models import Product
from profiles.models import UserProfile


def add_review(request, product_id):
    """
    Allow user to add a review and redirect them back to the
    item product item view
    """
    user = UserProfile.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    review_form = ReviewForm()
    review_details = {
        'title': request.POST['title'],
        'description': request.POST['description'],
        'rating': request.POST['rating'],
    }
    review_form = ReviewForm(review_details)

    # If form is valid, add user and product and save
    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.user = user
        review.product = product
        review.save()
        messages.success(request, 'Thank you! Your review was added')
    else:
        messages.error(request, 'Something went wrong. '
                                'Make sure the form is valid.')

    return redirect(reverse('product_details', args=(product_id,)))
