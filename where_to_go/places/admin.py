from django.contrib import admin

from .models import (
    Image,
    Place,
)


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ['get_preview', ]
    fields = ['name', 'get_preview', 'position']

    def get_preview(self, obj):
        return obj.get_preview


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
