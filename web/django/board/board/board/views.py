from django.shortcuts import render,get_object_or_404,redirect
from .models import Question,Answer
from .forms import QuestionForm,AnswerForm

from django.core.paginator import Paginator

def index(request):
    """
    Question 전체 목록 추출(작성날짜 최신순)
    """

    #현재 페이지 번호
    page = request.GET.get('page',1)

    question_list = Question.objects.order_by("-created_at")

    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)


    return render(request, "board/question_list.html",{"question_list":page_obj})

def detail(request, question_id):
    """
    question_id 에 맞는 질문 상세 추출
    """

    question = get_object_or_404(Question, id=question_id)

    return render(request, "board/question_detail.html",{"question":question})


def question_create(request):
    """
    get: 비어 있는 폼, post : 바인딩 폼
    """
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = QuestionForm()
    return render(request, "board/question_form.html",{"form":form})



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
            answer.save()
            return redirect("detail", question_id=question_id)
    else:
        form = AnswerForm()

    return render(request,"board/question_detail.html",{"form":form,"question":question})

