from django.shortcuts import render, redirect, get_object_or_404

from .models import Board
from .forms import BoardForm

from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator

def board_list(request):
    """
    Board 목록 전체 추출
    """
    # 전체 게시물 추출
    all_boards = Board.objects.order_by('-registered_dttm')
    
    # 사용자가 요청한 페이지 번호
    page = request.GET.get('page', 1) # 페이지가 없으면 1페이지를 보여줌
    
    # Paginator 객체를 이용한 보여줄 페이지 결정
    paginator = Paginator(all_boards, 10) # 한 페이지에 10개씩 보여줌
    
    boards = paginator.get_page(page)
    
    return render(request, 'board/board_list.html', {'boards': boards})

@login_required(login_url='login')
def board_write(request):
    """
    Board 새글 작성
    get : 비어있는 폼 / post : 바인딩 된 폼
    """
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False) # user 정보가 없으므로 임시 저장
            board.writer = request.user # user 정보 추가
            board.save()
            
            # 태그저장
            form.save_m2m()
            
            return redirect('board_list')
    else:
        form = BoardForm()
        
    return render(request, 'board/board_create.html', {'form': form})

def board_detail(request,pk):
    """
    상세보기
    """
    
    board = get_object_or_404(Board, pk=pk)
    
    return render(request, 'board/board_detail.html', {'board': board})