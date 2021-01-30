from django.contrib import admin
from .models import ContentReadyToDownload, Image_upload


class ContentReadyToDownloadAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'sku'
    )


class Image_uploadAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'title',
        'downloaded'
    )

    ordering = ('sku',)


admin.site.register(ContentReadyToDownload, ContentReadyToDownloadAdmin)
admin.site.register(Image_upload, Image_uploadAdmin)
