from django import template

from board.models import Post
from ..models import User

register = template.Library()


@register.simple_tag
def recent_post(count, uid):
    id = User.objects.get(id=uid)
    posts = Post.objects.filter(author=id).order_by('-create_date')[:count]
    return posts

@register.simple_tag
def count_post(uid):
    id = User.objects.get(id=uid)
    posts = Post.objects.filter(author=id).count()
    return posts
