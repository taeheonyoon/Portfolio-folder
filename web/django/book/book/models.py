from django.db import models

# book 테이블
# 도서코드(pk-문자), 도서명, 저자, 가격, 등록날자

class Book(models.Model):
    code = models.CharField(primary_key=True, max_length=4, verbose_name='도서코드')
    title = models.CharField(max_length=100, verbose_name='도서명')
    author = models.CharField(max_length=50, verbose_name='저자')
    price = models.IntegerField(verbose_name='도서정가')
    register_dttm = models.DateTimeField(verbose_name='등록날자', auto_now_add=True)
    
    
    class Meta:
        db_table = 'bookbl' # 생성되는 테이블 명 지정(기본값은 앱이름_book)