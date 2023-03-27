from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostForm

def post_list(request):
    """
    전체 글 목록 추출
    """
    # order_by:작성날짜 최신순

    posts = Post.objects.order_by('-created_at')

    return render(request,"blog/post_list.html",{"posts":posts})

@login_required(login_url="login")
def post_write(request):
    """
    글 작성 : 로그인 필수
    get - 빈 폼 / post - 바인딩 폼
    """
    if request.method == "POST":
        # request.POST : text 가져옴, request.FILES : file 가져옴
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False) 
            # 글쓴이 추가(== 로그인 사용자)
            post.user = request.user
            post.save()

            return redirect("post_list")
    else:
        form = PostForm()

    return render(request,"blog/post_write.html",{"form":form})


def post_detail(request,pk):
    """
    pk에 해당하는 글 조회
    """
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html",{"post":post})