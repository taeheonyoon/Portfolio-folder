from django import template
from users.models import User
from board.models import Post
register = template.Library()


@register.filter
def sub(value, arg):
    return value - arg

@register.simple_tag
def rank_post(count):
    ids = User.objects.all().count()
    post_num = []
    
    for uid in range(1, ids+1):
        id = User.objects.get(id=uid)
        name = User.objects.filter(id=uid).values_list('name')[0][0]
        postnum = Post.objects.filter(author=id).count()
        post_num.append((name, postnum))
        
    post_num.sort(key=lambda x:-x[1])
    posts = post_num[:count]
    return posts 