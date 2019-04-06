from django.contrib import admin

from shortener.models import Url


class UrlsAdmin(admin.ModelAdmin):
    list_display = ('url_code', 'full_url', 'creation_date')
    ordering = ('-creation_date',)


admin.site.register(Url, UrlsAdmin)
