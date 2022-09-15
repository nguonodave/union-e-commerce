from django.contrib import admin
from . models import Product

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('product_name', 'category', 'price', 'stock', 'created_date', 'modified_date', 'is_available') # fields to be displayed at the front page of the table in the database dashboard


admin.site.register(Product, ProductAdmin)
