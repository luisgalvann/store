from django import forms
from django.contrib.auth.models import User
from .models import ShippingAddress



class UserInfoForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ShippingInfoForm(forms.ModelForm):

    class Meta:
        model = ShippingAddress
        fields = ['name', 'address', 'city', 'country', 'zipcode']
