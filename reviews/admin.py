from django.contrib import admin
from .models import Review

# Register your models here.


class ReviewsAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'review_rating',

    )

    ordering = ('-review_rating',)


admin.site.register(Review, ReviewsAdmin)
