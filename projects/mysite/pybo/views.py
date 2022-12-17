from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Question

def index(request):

    '''
    pybo 목록 출력
    '''
    
    question_list = Question.objects.order_by('-create_date') # - 를 붙임으로 써 역순 정렬
    context = {'question_list': question_list}

    return render(request, 'pybo/question_list.html',context)

def detail(request, question_id):

    '''
    pybo 내용 출력
    '''

    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(request, 'pybo/question_detail.html',context)
