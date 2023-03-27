from django.contrib import admin
from .models import PlayMenu


class PlayMenuAdmin(admin.ModelAdmin):
    list_display = ["name","image","click_count" ]

admin.site.register(PlayMenu)