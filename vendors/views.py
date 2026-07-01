from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import VendorForm
from .models import Vendor


@login_required
def vendor_register(request):

    if request.user.role != "vendor":
        return redirect('/')

    if request.method == "POST":

        form = VendorForm(request.POST)

        if form.is_valid():

            vendor = form.save(commit=False)
            vendor.user = request.user
            vendor.save()

            return redirect('/vendors/dashboard/')

    else:
        form = VendorForm()

    return render(
        request,
        'vendors/vendor_register.html',
        {'form': form}
    )


@login_required
def vendor_dashboard(request):

    vendor = Vendor.objects.get(user=request.user)

    context = {
        'vendor': vendor
    }

    return render(
        request,
        'vendors/vendor_dashboard.html',
        context
    )