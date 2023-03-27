from django.shortcuts import render, redirect, get_object_or_404
from .forms import NameForm, MusicianForm
from .models import Musician
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

# 함수형 뷰
def index(request):
    return render(request, 'exam/index.html')

def custom_form(request):
    """
    get / post
    """
    
    errors = []
    
    if request.method == 'POST':
        # name 가져오기
        name = request.POST['name'] # request.POST.get('name')
        print(name)
        # 유효성 검증 - 이름이 홍길동이어야 한다.
        if name != '홍길동':
            #에러메세지 전송 - 원래 페이지로 돌려보내기
            errors.append("이름을 확인해 주세요")

        else:
            return redirect("index")
        
    
    
    
    return render(request, 'exam/custom_form.html', {'errors': errors})


def django_form(request):
    """
    get / post
    """
    
    if request.method == 'POST':
        # 사용자의 입력값을 폼 데이터로 수신
        form = NameForm(request.POST)
        if form.is_valid(): # 바인딩 여부, mx_length, required 검증
            return redirect("index")
    else:
        # 빈 폼을 하나 생성 후 전송
        form = NameForm()
    
    
    
    return render(request, 'exam/django_form.html', {'form': form})


# musician 추가
def musician_create(request):
    """
    get : 빈 폼을 전송
    post : 유효성 검증 후 저장
    """
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid(): # 바인딩 여부, mx_length, blank, null => False 검증
            form.save()
            return redirect('index')
    else:
        form = MusicianForm()
        
    return render(request, 'exam/create.html', {'form': form})

# musician 삭제
def musician_remove(request, pk):
    """
    pk에 해당하는 musician를 삭제
    """
    # pk 뮤지션 찾기
    musician = get_object_or_404(Musician, pk=pk)
    
    # 삭제 - delete()
    musician.delete()
    
    # redirect
    return redirect('musician_function_list')


# musician 수정
def musician_edit(request, pk):
    """
    get : pk에 해당하는 musician를 조회해서 폼에 담아서 전송
    post : 수정된 데이터 form으로 받아서 저장
    """
    musician = get_object_or_404(Musician, pk=pk)
    
    if request.method == 'POST':
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            musician = form.save()
            return redirect('musician_function_detail', pk=musician.pk)
    else:
        form = MusicianForm(instance=musician)
    return render(request, 'exam/edit.html', {'form': form})


# musician 전체 조회
def musician_list(request):
    """
    전체 musician 추출후 전송
    """
    # all
    list = Musician.objects.all()
    
    # render
    return render(request, 'exam/list.html', {'list': list})

# musician 한명 조회
def musician_detail(request, pk):
    """
    pk에 해당하는 musician 조회후 전송
    1. 조회, 전송 => 템플릿 파일을 처음부터 디자인
    2. 조회, form에 담기, 전송 => 템플릿 파일에서 form.as_p or for문 돌려서 만들기
    """
    # get_object_or_404
    musician = get_object_or_404(Musician, pk=pk)
    
    form = MusicianForm(instance=musician)
    
    # render
    #return render(request, 'exam/detail.html', {'musician': musician})
    return render(request, 'exam/detail.html', {'form': form})


##### 클래스 뷰
# TemplateView == render
# RedirectView == redirect
# ListView == 모델 설정

class SampleView(TemplateView):
    template_name = 'exam/sample.html'
    
    
class MusicianListView(ListView):
    model = Musician
    template_name = 'exam/list.html' # exam/musican_list.html
    context_object_name = 'list' # 생략 가능(단, 모델소문자_list.html 템플릿 파일을 생성했다면 )
    
class MusicianDetailView(DetailView):
    model = Musician
    template_name = 'exam/musician_detail.html'
    #context_object_name = 'musician'
    
class MusicianCreateView(CreateView):
    template_name = 'exam/create.html'
    form_class = MusicianForm
    success_url = reverse_lazy('musician_class_list')
    
class MusicianUpdateView(UpdateView):
    template_name = 'exam/edit.html'
    model = Musician
    fields = '__all__'
    context_object_name = 'form'
    
    # 성공시 pk를 가지고 detail 로 이동
    def get_success_url(self) -> str:
        return reverse_lazy('musician_class_detail', args=[self.object.pk])
    
class MusicianDeleteView(DeleteView):
    """
    DeleteView 에서 정의되어 있는 상태로는 삭제를 위한 폼을 사용하도록 되어 있음
    post 로 들어오는 요청에 대해 삭제 친행 => get 방식으로 들어와도 삭제할 수 있도록 변경
    """
    
    model = Musician
    success_url = reverse_lazy('musician_class_list')
    #template_name = "musician.delete.html"
    
    # get 오버라이딩
    
    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)