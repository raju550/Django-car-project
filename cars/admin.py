from django.contrib import admin
from .models import Car
from django.utils.html import format_html


# Register your models here.
class CarAdmin(admin.ModelAdmin):
    def thamnail(self, objects):
        return format_html('<img src="{}" width="40" style="border-radius:50px;"/>'.format(objects.car_photo.url))

    thamnail.short_description = 'Car Image'
    list_display = (
    'id', 'thamnail', 'car_title', 'city', 'color', 'model', 'year', 'body_style', 'fuel_type', 'is_features')
    list_display_links = ('id', 'thamnail', 'car_title')
    list_editable = ['is_features']
    search_fields = ('car_title', 'city', 'color', 'model', 'year', 'fuel_type')
    list_filter = ('city','model','fuel_type')


admin.site.register(Car, CarAdmin)
