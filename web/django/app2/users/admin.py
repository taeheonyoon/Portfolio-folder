from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'nickname']
    
    
admin.site.register(User, UserAdmin)