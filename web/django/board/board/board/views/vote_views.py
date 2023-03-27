from django.shortcuts import render,get_object_or_404,redirect
from ..models import Question,Answer
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url="login")
def vote_question(request,question_id):
    """
    질문 추천 등록 / 성공 시 detail
    질문찾은 후 question.voter.add(로그인 사용자)
    """

    question = get_object_or_404(Question, id=question_id)

    # 자신의 글은 추천하지 못하고 타인이 쓴 글만 추천 가능
    if question.author != request.user:
        question.voter.add(request.user)
    else:
        messages.error(request, "본인이 작성한 글은 추천할 수 없습니다.")

    return redirect("detail", question_id=question_id)

@login_required(login_url="login")
def vote_answer(request,answer_id):
    """
    답변 추천 등록 / 성공 시 detail
    답변 찾은 후 answer.voter.add(로그인 사용자)
    """

    answer = get_object_or_404(Answer, id=answer_id)

    # 자신의 글은 추천하지 못하고 타인이 쓴 글만 추천 가능
    if answer.author != request.user:
        answer.voter.add(request.user)
    else:
        messages.error(request, "본인이 작성한 글은 추천할 수 없습니다.")

    return redirect("detail", question_id = answer.question.id)