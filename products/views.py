from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Product
from .forms import ProductForm
from vendors.models import Vendor


@login_required
def product_list(request):

    vendor = Vendor.objects.get(user=request.user)

    products = Product.objects.filter(
        vendor=vendor
    )

    context = {
        'products': products
    }

    return render(
        request,
        'products/product_list.html',
        context
    )


@login_required
def add_product(request):

    vendor = Vendor.objects.get(user=request.user)

    if request.method == "POST":

        form = ProductForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            product = form.save(commit=False)

            product.vendor = vendor

            product.save()

            return redirect('/products/')

    else:

        form = ProductForm()

    return render(
        request,
        'products/add_product.html',
        {'form': form}
    )


@login_required
def edit_product(request, pk):

    vendor = Vendor.objects.get(user=request.user)

    product = get_object_or_404(
        Product,
        id=pk,
        vendor=vendor
    )

    if request.method == "POST":

        form = ProductForm(
            request.POST,
            request.FILES,
            instance=product
        )

        if form.is_valid():
            form.save()
            return redirect('/products/')

    else:
        form = ProductForm(instance=product)

    return render(
        request,
        'products/edit_product.html',
        {
            'form': form
        }
    )


@login_required
def delete_product(request, pk):

    vendor = Vendor.objects.get(user=request.user)

    product = get_object_or_404(
        Product,
        id=pk,
        vendor=vendor
    )

    product.delete()

    return redirect('/products/')

@login_required
def profile_view(request):

    if request.user.is_superuser:
        return redirect('/admin/')

    return render(
        request,
        'accounts/profile.html'
    )