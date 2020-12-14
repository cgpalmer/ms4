from django.contrib import admin
from .models import Product, Category, Special, Image_upload

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

class Image_uploadAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'title',
        'downloaded'
    )

    ordering = ('sku',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Special, SpecialAdmin)
admin.site.register(Image_upload, Image_uploadAdmin)

