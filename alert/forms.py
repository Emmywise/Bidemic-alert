from django import forms
from django.forms import ModelForm, fields
from .models import *

class marchantForm(forms.ModelForm): #merchant form
    class Meta:
        model = Merchant
        fields = '__all__'


class ProductForm(forms.ModelForm): #product form
    class Meta:
        model = Product
        fields = '__all__'
