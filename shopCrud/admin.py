from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'price', 'stock', 'image']

admin.site.register(Product)