from django.shortcuts import render,get_object_or_404,redirect,resolve_url
from ..models import Question,Answer,Comment
from ..forms import CommentForm
from django.contrib.auth.decorators import login_required

######### comment
@login_required(login_url="login")
def comment_question_create(request,question_id):
    """
    CommentForm, get, post, 성공시 detail 이동
    """
    question = get_object_or_404(Question, id=question_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.question = question
            comment.save()
            # return redirect("detail", question_id=question_id)

            return redirect("{}#comment_{}".format(resolve_url("detail",question_id=question_id),comment.id))  # http://127.0.0.1:8000/board/310/#comment_15
    else:
        form = CommentForm()

    return render(request, "board/comment_form.html",{"form":form})

@login_required(login_url="login")
def comment_question_update(request, comment_id):
    """
    댓글 내용 수정 - CommentForm,get,post, 성공 시 detail,comment_form.html 사용
    """
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            # return redirect("detail", question_id=comment.question.id)
            return redirect("{}#comment_{}".format(resolve_url("detail",question_id=comment.question.id),comment.id))
    else:
        form = CommentForm(instance=comment)

    return render(request, "board/comment_form.html",{"form":form})

@login_required(login_url="login")
def comment_question_delete(request, comment_id):
    """
    댓글 내용 삭제 - get 성공 시 detail
    """

    comment = get_object_or_404(Comment, id=comment_id)

    comment.delete()

    return redirect("detail", question_id=comment.question.id)


@login_required(login_url="login")
def comment_answer_create(request,answer_id):
    """
    답변 댓글 추가 - CommentForm, get, post, 성공시 detail 이동
    """
    answer = get_object_or_404(Answer, id=answer_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.answer = answer
            comment.save()
            # return redirect("detail", question_id=answer.question.id)
            return redirect("{}#comment_{}".format(resolve_url("detail",question_id=answer.question.id),comment.id)) 
    else:
        form = CommentForm()

    return render(request, "board/comment_form.html",{"form":form})

@login_required(login_url="login")
def comment_answer_update(request, comment_id):
    """
    답변 댓글 내용 수정 - CommentForm,get,post, 성공 시 detail,comment_form.html 사용
    """
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            # return redirect("detail", question_id=comment.answer.question.id)
            return redirect("{}#comment_{}".format(resolve_url("detail",question_id=comment.answer.question.id),comment.id)) 
    else:
        form = CommentForm(instance=comment)

    return render(request, "board/comment_form.html",{"form":form})

@login_required(login_url="login")
def comment_answer_delete(request, comment_id):
    """
    답변 댓글 내용 삭제 - get 성공 시 detail
    """

    comment = get_object_or_404(Comment, id=comment_id)

    comment.delete()

    return redirect("detail", question_id=comment.answer.question.id)