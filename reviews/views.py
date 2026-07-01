from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib.auth.decorators import login_required

from products.models import Product
from .models import Review


@login_required
def add_review(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":

        rating = int(request.POST.get('rating'))
        comment = request.POST.get('comment')

        review = Review.objects.filter(
            user=request.user,
            product=product
        ).first()

        if review:
            review.rating = rating
            review.comment = comment
            review.save()
        else:
            Review.objects.create(
                user=request.user,
                product=product,
                rating=rating,
                comment=comment
            )

        return redirect(f'/product/{product.slug}/')


@login_required
def delete_review(request, review_id):

    review = get_object_or_404(
        Review,
        id=review_id,
        user=request.user
    )

    product_slug = review.product.slug

    review.delete()

    return redirect(
        f'/product/{product_slug}/'
    )