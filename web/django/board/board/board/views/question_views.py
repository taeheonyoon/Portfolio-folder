from django.shortcuts import render,get_object_or_404,redirect
from ..models import Question
from ..forms import QuestionForm
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def question_create(request):
    """
    get: 비어 있는 폼, post : 바인딩 폼
    """
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect("index")
    else:
        form = QuestionForm()
    return render(request, "board/question_form.html",{"form":form})

@login_required(login_url="login")
def question_update(request,question_id):
    """
    질문 수정 - form 사용, 수정이 완료된 후 detail 이동
    """
    # 수정 질문 찾기
    question = get_object_or_404(Question, id=question_id)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect("detail",question_id=question_id)
    else:
        form = QuestionForm(instance=question)
    return render(request, "board/question_update.html", {"form":form})

@login_required(login_url="login")
def question_delete(request,question_id):
    """
    question_id 값과 일치한 질문 삭제 후 전체 리스트
    """
    # 삭제 질문 찾기
    question = get_object_or_404(Question, id=question_id)

    if request.user != question.author:
        return redirect("detail", question_id=question_id)
    
    question.delete()    
    return redirect("index")
