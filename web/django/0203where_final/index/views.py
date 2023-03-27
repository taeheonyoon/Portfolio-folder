from django.shortcuts import render, get_object_or_404
from board.models import Post

# Create your views here.

def index(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {'post':post}
    return render (request, 'index/index.html', context)