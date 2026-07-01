from django.shortcuts import render
from products.models import Product


def search_product(request):

    query = request.GET.get('q')

    products = Product.objects.filter(
        name__icontains=query,
        is_active=True,
        is_approved=True
    )

    context = {
        'products': products,
        'query': query
    }

    return render(
        request,
        'search_results.html',
        context
    )