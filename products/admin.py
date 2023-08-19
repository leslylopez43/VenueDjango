from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'get_category',  # Use a method to display the category name
        'price',
        'rating',
        'image'
    )

    ordering = ('sku',)

    def get_category(self, obj):
        return obj.category.name if obj.category else None
    get_category.short_description = 'Category'

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )   

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

