from django.shortcuts import render, redirect,get_object_or_404
from .models import Review, Store
from django.http import HttpResponse
from django.db.models import Count, Avg
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm

def storelist(request):
    stores = Store.objects.all().annotate(reviews_count=Count('review')).annotate(average_grade=Avg('review__grade'))
    context = {'stores': stores}
    return render(request, 'review/storelist.html', context)


def review(request, pk):
    store = Store.objects.get(id=pk)
    # store = get_object_or_404(Store, id=pk)
    form = ReviewForm()
    context = {'store': store, 'form': form}
    
    return render(request, 'review/review.html', context)


@login_required(login_url='users:login')
def comments_create(request, pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=pk)
        comment_form = ReviewForm(request.POST,request.FILES)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.store = review.store
            comment.user = request.user
            comment.save()
        return redirect('review:review', review.pk)
    return redirect('login')


@login_required(login_url='users:login')
def comments_delete(request, comment_id):
    comment = get_object_or_404(Review, pk=comment_id)
    # if request.user != comment.author and not request.user.is_staff :
    #     messages.error(request, '삭제권한이 없습니다') 
    # else:  
    #     comment.delete()
    return redirect('review:review', comment.review.pk)