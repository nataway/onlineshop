# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# from orders.models import Order
from shop.models import Product
from accounts.models import User

# Create your models here.
class PaymentModel(models.Model):
    # _id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=250,null=True)
    # order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return '{}'.format(self.id)

class ShippingAddress(models.Model):
    # order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    # _id = models.AutoField(primary_key=True, editable=False)
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100, null=True) 
    state = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.id)

class Review(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    rating = models.TextField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '{}'.format(self.product.name)
