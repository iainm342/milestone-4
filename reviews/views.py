from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .models import Review
from .forms import ReviewForm
from products.models import Product
from profiles.models import UserProfile


def add_review(request, product_id):
    """
    Add a review to a product
    """
    product = get_object_or_404(Product, pk=product_id)
    user = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            rating = form.cleaned_data['rating']
            Review.objects.create(
                user=user,
                product=get_object_or_404(Product, pk=product_id),
                title=title,
                rating=rating,
                description=description)
            messages.success(request, 'Successfully added review.')
            return redirect(reverse('product_detail', args=[product_id]))
        else:
            messages.error(request, 'Failed to add review. \
                    Please check the form is valid and try again.')
    else:
        form = ReviewForm()
    template = 'reviews/add_review.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


def edit_review(request, review_id):
    """
    Edit a review to a product
    """
    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully edited review.')
        else:
            messages.error(request, 'Failed to edit review. \
                    Please check the form is valid and try again.')
    else:
        form = ReviewForm(instance=review)

    template = "reviews/edit_review.html"
    context = {
        "form": form,
        "review": review,
        "product": review.product,
    }

    return render(request, template, context)


def delete_review(request, review_id):
    """
    Delete a review for a product
    """
    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    messages.success(request, 'Review deleted!')
    return redirect(reverse('product_detail', args=(review.product.id,)))
