from django import forms

class SubnetForm(forms.Form):
    ip_address = forms.GenericIPAddressField()
    subnet_mask = forms.GenericIPAddressField()
    subnet_bits = forms.IntegerField(min_value=0, max_value=32)
