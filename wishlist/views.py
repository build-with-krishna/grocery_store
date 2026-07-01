from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Wishlist
from products.models import Product

from cart.models import Cart, CartItem


@login_required
def wishlist_view(request):

    items = Wishlist.objects.filter(
        user=request.user
    )

    return render(
        request,
        'wishlist/wishlist.html',
        {
            'items': items
        }
    )


@login_required
def add_to_wishlist(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    Wishlist.objects.get_or_create(
        user=request.user,
        product=product
    )

    return redirect('/wishlist/')


@login_required
def remove_from_wishlist(request, id):

    item = get_object_or_404(
        Wishlist,
        id=id,
        user=request.user
    )

    item.delete()

    return redirect('/wishlist/')


@login_required
def move_to_cart(request, id):

    item = get_object_or_404(
        Wishlist,
        id=id,
        user=request.user
    )

    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=item.product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    item.delete()

    return redirect('/cart/')