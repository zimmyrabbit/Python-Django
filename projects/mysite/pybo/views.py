from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from .models import Answer
from django.utils import timezone
from .forms import QuestionForm, AnswerFrom
from django.core.paginator import Paginator

def index(request):
    '''
    pybo 목록 출력
    '''
    page = request.GET.get('page','1')
    
    question_list = Question.objects.order_by('-create_date') # - 를 붙임으로 써 역순 정렬

    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}

    return render(request, 'pybo/question_list.html',context)

def detail(request, question_id):
    '''
    pybo 내용 출력
    '''

    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(request, 'pybo/question_detail.html',context)

def answer_create(request, question_id):
    '''
    pybo 답변 등록
    '''
    
    question = get_object_or_404(Question, pk=question_id)
    ##question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())

    #answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    #answer.save()

    #return redirect('pybo:detail', question_id=question.id)

    if request.method == 'POST':
        form = AnswerFrom(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerFrom()
    
    context = {'question':question, 'form':form}
    return render(request, 'pybo/question_detail.html', context)

def question_create(request):
    '''
    pybo 질문 등록
    '''

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else :
        form = QuestionForm()

    context = {'form' : form}
    return render(request, 'pybo/question_form.html', context)

