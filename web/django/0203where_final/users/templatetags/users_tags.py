from django import template

from board.models import Post
from review.models import Review
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

@register.simple_tag
def recent_review(count, uid):
    id = User.objects.get(id=uid)
    reviews = Review.objects.filter(user=id).order_by('-created_at')[:count]
    return reviews

@register.simple_tag
def count_review(uid):
    id = User.objects.get(id=uid)
    reviews = Review.objects.filter(user=id).count()
    return reviews
