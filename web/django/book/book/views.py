from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Book
from .forms import BookForm

def list(request):
    """
    전체 도서 목록 추출
    """
    book_list = Book.objects.all()

    
    return render(request, 'book/book_list.html', {'book_list': book_list})

def detail(request, pk):
    """
    pk에 해당하는 상세 정보 추출
    """
    book_detail = get_object_or_404(Book, pk=pk)
    return render(request, 'book/book_detail.html', {'book_detail': book_detail})

def update(request, pk):
    """
    get : pk에 해당하는 상세 정보 수정
    post : 정보 수정
    """
    book_detail = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book_detail)
        if form.is_valid():
            form.save()
            return redirect('detail', pk=book_detail.pk)
    else:
        form = BookForm(instance=book_detail)
    return render(request, 'book/book_update.html', {'form': form})

def remove(request, pk):
    """
    pk에 해당하는 도서 정보 삭제
    """
    book_detail = get_object_or_404(Book, pk=pk)
    book_detail.delete()
    return redirect('list')

def create(request):
    """
    get : 북폼 비어잇는 상태로
    post : 북폰에 입력값 바인딩 후 저장 후 목록으로
    """
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = BookForm()
    return render(request, 'book/book_create.html', {'form': form})