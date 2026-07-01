from django.shortcuts import render, get_object_or_404
from products.models import Product
from category.models import Category


def home(request):

    products = Product.objects.filter(
        is_active=True,
        is_approved=True
    ).order_by('-id')

    categories = Category.objects.filter(
        is_active=True
    )

    context = {
        'products': products,
        'categories': categories
    }

    return render(
        request,
        'home.html',
        context
    )


def product_detail(request, slug):

    product = get_object_or_404(
        Product,
        slug=slug,
        is_approved=True
    )

    reviews = product.reviews.all()

    avg_rating = 0

    if reviews.exists():

        total = 0

        for r in reviews:
            total += r.rating

        avg_rating = total / reviews.count()

    return render(
        request,
        'product_detail.html',
        {
            'product': product,
            'reviews': reviews,
            'avg_rating': avg_rating
        }
    )