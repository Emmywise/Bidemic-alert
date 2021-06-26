from django.db import models
from django.utils import timezone
# Create your models here.

class Merchant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    salutation = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % self.first_name

class Product(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    product_alert = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField( null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % self.merchant
   

