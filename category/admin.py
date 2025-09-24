from django.contrib import admin
from .models import Category



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'category_slug', 'category_description', 'category_created_date', 'category_updated_date')
    prepopulated_fields = {'category_slug': ('category_name',)}  # Auto-fill slug field based on category name
    search_fields = ('category_name', 'category_description')  # Add search functionality
    list_filter = ('category_created_date', 'category_updated_date')  # Add filters for created and updated dates

# Register your models here.
admin.site.register(Category, CategoryAdmin)