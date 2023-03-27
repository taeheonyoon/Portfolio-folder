from django import template

from board.models import Post

register = template.Library()


@register.simple_tag
def recent_eat(count):
    post = Post.objects.filter(category_id = 2).order_by('-create_date')[:count]
    return post

@register.simple_tag
def recent_drink(count):
    post = Post.objects.filter(category_id = 3).order_by('-create_date')[:count]
    return post

@register.simple_tag
def recent_do(count):
    post = Post.objects.filter(category_id = 4).order_by('-create_date')[:count]
    return post