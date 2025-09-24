from django.contrib import admin
from .models import product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_price', 'product_stock', 'product_created_date', 'product_updated_date')
    prepopulated_fields = {'product_slug': ('product_name',)}  # Auto-fill slug field based on product name
    search_fields = ('product_name', 'product_description')  # Add search functionality
    list_filter = ('product_created_date', 'product_updated_date')  # Add filters for created and updated dates

# Register your models here.
admin.site.register(product , ProductAdmin)