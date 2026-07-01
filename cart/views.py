from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Cart, CartItem
from products.models import Product


@login_required
def add_to_cart(request, product_id):

    if request.user.role != "customer":
        return redirect('/')

    product = get_object_or_404(Product, id=product_id)

    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created:
        item.quantity += 1
        item.save()

    return redirect('/cart/')


@login_required
def cart_view(request):

    if request.user.role != "customer":
        return redirect('/')

    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    items = cart.items.all()

    total = sum(item.subtotal for item in items)

    return render(
        request,
        'cart/cart.html',
        {
            'items': items,
            'total': total
        }
    )


@login_required
def increase_quantity(request, item_id):

    if request.user.role != "customer":
        return redirect('/')

    item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user
    )

    item.quantity += 1
    item.save()

    return redirect('/cart/')


@login_required
def decrease_quantity(request, item_id):

    if request.user.role != "customer":
        return redirect('/')

    item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user
    )

    if item.quantity > 1:
        item.quantity -= 1
        item.save()

    return redirect('/cart/')


@login_required
def remove_item(request, item_id):

    if request.user.role != "customer":
        return redirect('/')

    item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user
    )

    item.delete()

    return redirect('/cart/')