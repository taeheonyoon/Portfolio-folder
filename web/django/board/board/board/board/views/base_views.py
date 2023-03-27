from django.shortcuts import render,get_object_or_404
from ..models import Question,QuestionCount
from django.core.paginator import Paginator
from django.db.models import Q,Count
from tools.utils import get_client_ip


def index(request):
    """
    Question 전체 목록 추출(작성날짜 최신순)
    """

    # 현재 페이지 번호
    page = request.GET.get('page',1)
    # 검색어 받기
    keyword = request.GET.get('keyword','') # request.GET['keyword']
    # 정렬기준 받기
    so = request.GET.get('so','recent')  # sort 기준 : recent(기본),recommend,popular


    print("keyword",keyword)

    if so == "recommend":
        question_list = Question.objects.annotate(num_voter = Count('voter')).order_by("-num_voter","-created_at")
    elif so == "popular":
        question_list = Question.objects.annotate(num_answer = Count('answer')).order_by("-num_answer","-created_at")
    else:
        question_list = Question.objects.order_by("-created_at")



    # 전체 리스트에서 검색어가 들어간 리스트만 추출 : 질문 제목, 질문 내용, 질문작성자, 답변 작성자
    # Q : OR 조건으로 데이터 조회,  distinct() : 중복 제거
    if keyword:
        question_list = question_list.filter(
            Q(subject__icontains=keyword) | 
            Q(content__icontains=keyword) | 
            Q(author__username__icontains=keyword) |
            Q(answer__author__username__icontains=keyword)).distinct()

    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)


    return render(request, "board/question_list.html",{"question_list":page_obj, "page":page, "keyword":keyword, "so":so})

def detail(request, question_id):
    """
    question_id 에 맞는 질문 상세 추출
    조회수 증가 : ip 얻어내기
    """

    # 현재 페이지 번호
    page = request.GET.get('page',1)
    # 검색어 받기
    keyword = request.GET.get('keyword','') # request.GET['keyword']
    # 정렬기준 받기
    so = request.GET.get('so','recent')  # sort 기준 : recent(기본),recommend,popular

    question = get_object_or_404(Question, id=question_id)


    # ip 가져오기
    ip = get_client_ip(request)
    # 현재 질문에 대한 조회수 찾기
    cnt = QuestionCount.objects.filter(ip=ip, question=question).count()

    if cnt == 0:
        qc = QuestionCount(ip=ip, question=question)
        qc.save()

        if question.view_cnt:
            question.view_cnt += 1
        else:
            question.view_cnt = 1
        question.save()

    return render(request, "board/question_detail.html",{"question":question,"page":page,"keyword":keyword,"so":so})