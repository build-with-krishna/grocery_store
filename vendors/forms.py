from django import forms
from .models import Vendor


class VendorForm(forms.ModelForm):

    class Meta:
        model = Vendor

        fields = [
            'shop_name',
            'gst_number',
            'pan_number',
            'bank_name',
            'account_number',
            'ifsc_code',
            'address'
        ]