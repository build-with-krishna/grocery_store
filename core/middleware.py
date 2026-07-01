from django.shortcuts import redirect
from django.urls import resolve


class RoleBasedAccessMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.user.is_authenticated:

            current_path = request.path

            # Super Admin
            if request.user.is_superuser:

                # Admin sirf admin panel access kare
                if not current_path.startswith('/admin'):
                    return redirect('/admin/')

            # Vendor
            elif request.user.role == "vendor":

                customer_urls = [

                    '/cart',
                    '/wishlist',
                    '/orders',
                    '/payments',

                ]

                for url in customer_urls:

                    if current_path.startswith(url):
                        return redirect('/dashboard/')

            # Customer
            elif request.user.role == "customer":

                vendor_urls = [

                    '/dashboard',
                    '/vendors/add-product',
                    '/vendors/products',

                ]

                for url in vendor_urls:

                    if current_path.startswith(url):
                        return redirect('/')

        response = self.get_response(request)

        return response