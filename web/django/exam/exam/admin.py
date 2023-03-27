from django.contrib import admin
from .models import Question, Choice

# 모델 사용하려면 어드민 사이트에 등록 필수
admin.site.register(Question)
admin.site.register(Choice)
