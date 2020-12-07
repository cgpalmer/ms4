from django.contrib import admin
from .models import ContentReadyToDownload

class ContentReadyToDownloadAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'sku'
    )

admin.site.register(ContentReadyToDownload, ContentReadyToDownloadAdmin)

