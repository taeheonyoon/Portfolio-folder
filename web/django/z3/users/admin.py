from django.contrib import admin
from .models import User, Profile, Content, Image

class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'phone']


class ImageInline(admin.TabularInline):
    model = Image

class ContentAdmin(admin.ModelAdmin):
    list_display = ['user', 'text']
    inlines = [ImageInline]

admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(Content, ContentAdmin)    

