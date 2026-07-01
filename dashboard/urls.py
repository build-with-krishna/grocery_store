from django.urls import path
from .views import *
from .views import dashboard_view,sales_report

urlpatterns = [

    path(
        '',
        dashboard_view,
        name='dashboard'
    ),

    path(
        'sales-report/',
        sales_report,
        name='sales_report'
    ),

]