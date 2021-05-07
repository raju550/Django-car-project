from django.contrib import admin
from .models import Team
from django.utils.html import format_html


# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def thamnail(self, objects):
        return format_html('<img src="{}" width="40" style="border-radius:50%;"/>'.format(objects.photo.url))
    thamnail.short_description = 'Photo'
    list_display = ('id','thamnail', 'fname', 'lname','designation')
    list_display_links = ('id', 'fname','designation')
    search_fields = ('fname','lname','designation')
    list_filter = ['designation']

admin.site.register(Team, TeamAdmin)
