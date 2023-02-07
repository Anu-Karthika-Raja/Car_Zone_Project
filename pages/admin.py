from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:45px"/>'.format(object.photo.url))
    thumbnail.short_description ="Photo"
    list_display=('thumbnail', 'first_name' ,'desigination', 'created_date')
    list_display_links =('thumbnail','first_name',)
    search_fields=('first_name','last_name', 'desigination')
    list_filter=('desigination',)
    
    
admin.site.register(Team,TeamAdmin)

