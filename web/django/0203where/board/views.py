from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment, Category
from .forms import PostForm, CommentForm
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from datetime import date, datetime, timedelta

def index(request, category_name='free'):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so','recent')
    
    category_list = Category.objects.all()
    category = get_object_or_404(Category, name=category_name)
    post_list = Post.objects.filter(category=category)
    post_notice = post_list.filter(notice=True)


    if so == "recommend":
        post_list = post_list.annotate(num_voter = Count('voter')).order_by("-num_voter","-create_date")
    elif so == "popular":
        post_list = post_list.annotate(num_comment = Count('comment')).order_by("-num_comment","-create_date")
    elif so == "viewed":
        post_list = post_list.order_by("-view_cnt","-create_date")
    else:
        post_list = post_list.order_by("-create_date")
        
    post_notice = post_notice.order_by("-create_date")
    
    if kw:
        post_list = post_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(comment__content__icontains=kw) |  # 답변 내용 검색
            Q(author__name__icontains=kw) |  # 제목 글쓴이 검색
            Q(comment__author__name__icontains=kw)  # 내용 글쓴이 검색
        ).distinct()
    paginator = Paginator(post_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    
    context = {'post_list': page_obj, 'page': page, 'kw': kw, 'category_list': category_list, 'category': category, "so":so, "post_notice":post_notice}
    return render(request, 'board/list.html', context)

def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    
    response = render(request, 'board/detail.html', context)
    
    expire_date, now = datetime.now(), datetime.now()
    expire_date += timedelta(days=1)
    expire_date = expire_date.replace(hour=0, minute=0, second=0, microsecond=0)
    expire_date -= now
    max_age = expire_date.total_seconds()
    
    cookie_value = request.COOKIES.get('viewcnt', '_')
    
    if f'_{post_id}_' not in cookie_value:
        cookie_value += f'{post_id}_'
        response.set_cookie('viewcnt', value=cookie_value, max_age=max_age, httponly=True)
        post.view_cnt += 1
        post.save()
        
    return response

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
    if len(request.POST.getlist('notice')) == 0:
        notice = False
    else: 
        notice = True
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.create_date = timezone.now()
            post.category = category
            post.notice = notice
            post.save()
            return redirect('board:index', category)
    else:
        form = PostForm()
    context = {'form': form, 'category': category}
    return render(request, 'board/post_form.html', context)

@login_required(login_url='users:login')
def modify(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if len(request.POST.getlist('notice')) == 0:
        notice = False
    else: 
        notice = True
    if request.user != post.author:
        messages.error(request, '자신의 글만 수정 가능합니다.')
        return redirect('board:detail', post_id=post.id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.modify_date = timezone.now()  # 수정일시 저장
            post.notice = notice
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
    return redirect('board:index', post.category)

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

