from django.contrib import admin
from .models import Product, Category, Special

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image_mobile',
        'special_offer'
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class SpecialAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'discounts',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Special, SpecialAdmin)
