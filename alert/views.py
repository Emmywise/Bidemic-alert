from alert.forms import marchantForm
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
from .forms import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


class MerchantView(APIView):

    def post(self, request): #post request for merchant class
        serializer = MerchantSerializer(data=request.data)
        if serializer.is_valid(): # check if data is valid
            serializer.save() # save the data collect
            return Response(serializer.data, status=status.HTTP_201_CREATED) #response status if successs
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # error status

    def get(self, request, format=None ): #get request for merchant class
        merchant = Merchant.objects.all() # get all the available data
        serializer = MerchantSerializer(merchant, many=True)
        return Response(serializer.data) #response to display data
        
def home(request):
    return render(request, 'alert/index.html') #rendering index page as home


def register_merchant(request):
    if request.method == 'POST':  # making sure its a post request
        form = marchantForm(request.POST)
        if form.is_valid():  # check if data is valid
            form.save()  # save the data collect
        return HttpResponseRedirect(reverse("view-merchant"))  # redirect to next page after saving file
    else:
        form = marchantForm
    return render(request, 'alert/register-merchant.html', {'form': form})

def Viewmerchant(request):
    merchants = Merchant.objects.filter().order_by('-id')[:10]  # filter inputed data by id
    return render(request, 'alert/view-merchant.html',{"merchants": merchants})


def register_product(request):
    if request.method == 'POST':  # making sure its a post request
        form = ProductForm(request.POST)
        if form.is_valid():  # check if data is valid
            form.save()  # save the data collect
        return HttpResponseRedirect(reverse("view-product"))  # redirect to next page after saving file
    else:
        form = ProductForm
    return render(request, 'alert/register-product.html', {'form': form})

def Viewproduct(request):
    products = Product.objects.filter().order_by('-id')[:10]  # filter inputed data by id
    return render(request, 'alert/view-product.html', {"products": products})
