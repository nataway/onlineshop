# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.contrib import admin
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(PaymentModel)
admin.site.register(ShippingAddress)
admin.site.register(Review)