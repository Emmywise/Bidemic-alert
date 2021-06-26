from alert.forms import marchantForm
from django.shortcuts import render
from .serializers import *
from .models import *
from .forms import *
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.views import APIView
# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


# class MerchantView(APIView):
#     # parser_class = (FileUploadParser,)
#     def post(self, request):
#         serializer = MerchantSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def home(request):
    return render(request, 'alert/index.html')


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
