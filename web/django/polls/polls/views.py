from django.shortcuts import render, get_object_or_404
from .models import Question, Choice

#Create your views here.
def index(request):
    """
    질문 전체 보기 구현
    """
    # 잘뮨 전체 리스트 : 가장 최신 질문 순으로
    # Question.objects.order_by('-pub_date') 오름차순
    question_list = Question.objects.order_by('-pub_date') # 내림차순
    # question_list = Question.objects.order_by('pub_date')[:5] # 내림차순 + 5개
    return render(request, 'polls/index.html', {'question_list': question_list})

def detail(request, pk):
    """
    pk에 해당하는 choice 필요, pk에 해당하는 question 필요
    
    question = Question.objects.get(pk=pk)
    choice = Choice.objects.filter(question_id=pk)
    """
    get_object_or_404(Question, pk=pk)
    return render(request, 'polls/detail.html', {'question': question})

def votes(request, pk):
    """
    pk에 해당하는 질문 가져오기
    질문을 통해 choice 에 접근한 후 투표수 증가
    사용자의 선택된 choice를 가져오기
    """
    question = Question.objects.get(pk=pk)
    
    if request.method == "POST":
        try:            
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except KeyError as e:
            return render(request, 'polls/detail.html', {"question": question, "error_message": "선택하지 않았습니다."})
        else:
            selected_choice.vote += 1
            selected_choice.save()
            return redirect("index")