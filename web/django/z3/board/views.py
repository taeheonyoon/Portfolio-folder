from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment, Category
from .forms import PostForm, CommentForm
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def index(request, category_name='free'):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    
    category_list = Category.objects.all()
    category = get_object_or_404(Category, name=category_name)
    post_list = Post.objects.filter(category=category)
    
    post_list = post_list.order_by('-create_date')
    if kw:
        post_list = post_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(comment__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(comment__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()
    paginator = Paginator(post_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'post_list': page_obj, 'page': page, 'kw': kw, 'category_list': category_list, 'category': category}
    return render(request, 'board/list.html', context)

def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'board/detail.html', context)

@login_required(login_url='users:login')
def comment_create(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.post = post
            comment.save()
            return redirect('board:detail', post_id=post.id)
    else:
        form = CommentForm()
    context = {'post': post, 'form': form}
    return render(request, 'board/detail.html', context)

@login_required(login_url='users:login')
def create(request, category_name):
    category = Category.objects.get(name=category_name)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.create_date = timezone.now()
            post.category = category
            post.save()
            return redirect('board:index')
    else:
        form = PostForm()
    context = {'form': form, 'category': category}
    return render(request, 'board/post_form.html', context)

@login_required(login_url='users:login')
def modify(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user != post.author:
        messages.error(request, '자신의 글만 수정 가능합니다.')
        return redirect('board:detail', post_id=post.id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.modify_date = timezone.now()  # 수정일시 저장
            post.save()
            return redirect('board:detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    context = {'form': form, 'category': post.category}
    return render(request, 'board/post_form.html', context)

@login_required(login_url='users:login')
def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user != post.author and not request.user.is_staff:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('board:detail', post_id=post.id)
    post.delete()
    return redirect('board:index')

@login_required(login_url='users:login')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author and not request.user.is_staff :
        messages.error(request, '삭제권한이 없습니다') 
    else:  
        comment.delete()
    return redirect('board:detail', post_id=comment.post.id)

@login_required(login_url='users:login')
def vote(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user == post.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        post.voter.add(request.user)
    return redirect('board:detail', post_id=post.id)

