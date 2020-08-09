from django.contrib import admin
from .models import product, imageslider, cart, Order

admin.site.register(product)
admin.site.register(imageslider)
admin.site.register(cart)
admin.site.register(Order)