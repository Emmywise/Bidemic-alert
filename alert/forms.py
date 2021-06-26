from django import forms
from django.forms import ModelForm, fields
from .models import *

class marchantForm(forms.ModelForm):
    class Meta:
        model = Merchant
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
