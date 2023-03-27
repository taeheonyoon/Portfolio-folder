from django.contrib import admin
from .models import Review, Store
from .forms import ReviewForm

# Register your models here.
admin.site.register(Store)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    form = ReviewForm


# admin.site.register(Review)