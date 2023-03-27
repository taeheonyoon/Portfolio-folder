from django.contrib import admin
from .models import Question, Answer,Comment

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('subject','created_at')

admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Comment)


