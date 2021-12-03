from adminsortable2.admin import SortableInlineAdminMixin

from django.contrib import admin

from .models import (
    Image,
    Place,
)


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 2
    fields = ['img', 'get_preview', 'position']
    readonly_fields = ['get_preview', ]

    def get_preview(self, obj):
        return obj.get_preview


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    search_fields = ('title_long', )
