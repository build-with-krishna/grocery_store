from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from vendors.models import Vendor
from products.models import Product
from orders.models import OrderItem


@login_required
def dashboard_view(request):

    if request.user.role != "vendor":
        return redirect('/')

    vendor = Vendor.objects.filter(
        user=request.user
    ).first()

    if not vendor:
        return redirect('/')

    products = Product.objects.filter(
        vendor=vendor
    )

    order_items = OrderItem.objects.filter(
        product__vendor=vendor
    )

    revenue = 0
    pending_orders = 0
    delivered_orders = 0

    for item in order_items:

        revenue += item.subtotal

        if item.order.status == "pending":
            pending_orders += 1

        elif item.order.status == "delivered":
            delivered_orders += 1

    context = {

        "total_products": products.count(),

        "total_orders": order_items.count(),

        "revenue": revenue,

        "pending_orders": pending_orders,

        "delivered_orders": delivered_orders,

        "latest_orders": order_items.order_by('-id')[:10]

    }

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )


@login_required
def sales_report(request):

    if request.user.role != "vendor":
        return redirect('/')

    vendor = Vendor.objects.filter(
        user=request.user
    ).first()

    if not vendor:
        return redirect('/')

    items = OrderItem.objects.filter(
        product__vendor=vendor
    ).order_by('-id')

    total_sales = sum(item.subtotal for item in items)

    return render(
        request,
        "dashboard/sales_report.html",
        {
            "items": items,
            "total_sales": total_sales
        }
    )