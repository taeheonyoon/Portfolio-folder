from django.shortcuts import render,get_object_or_404,redirect,resolve_url
from ..models import Question,Answer
from ..forms import AnswerForm
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def answer_create(request,question_id):
    """
    답변 등록 - get(비어 있는 폼) / post(바인딩 폼)
    """
    question = get_object_or_404(Question, pk=question_id)

    # question.answer_set.create(content=request.POST['content'])
    # answer = Answer(question=question, content=request.POST['content'])
    # answer.save()

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            # return redirect("detail", question_id=question_id)  # http://127.0.0.1:8000/board/310/
            return redirect("{}#answer_{}".format(resolve_url("detail",question_id=question_id),answer.id))  # http://127.0.0.1:8000/board/310/#answer_15
    else:
        form = AnswerForm()

    return render(request,"board/question_detail.html",{"form":form,"question":question})

@login_required(login_url="login")
def answer_update(request,answer_id):
    """
    답변 수정 - AnswerForm 사용(answer_form.html), 수정 성공 시 detail 로 이동
    """
    answer = get_object_or_404(Answer, id=answer_id)

    if request.user != answer.author:
        return redirect("detail", question_id=answer.question_id)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.save()

            # return redirect("detail", question_id=answer.question_id)
            return redirect("{}#answer_{}".format(resolve_url("detail",question_id=answer.question_id),answer.id))  # http://127.0.0.1:8000/board/310/#answer_15
    else:
        form = AnswerForm(instance=answer)

    return render(request, "board/answer_form.html", {"form":form})

@login_required(login_url="login")
def answer_delete(request,answer_id):
    """
    답변 삭제, 삭제 성공 시 detail 로 이동
    """
    answer = get_object_or_404(Answer, id=answer_id)

    if request.user != answer.author:
        return redirect("detail", question_id=answer.question_id)

    answer.delete()
    return redirect("detail", question_id=answer.question_id)
