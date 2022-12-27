from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count
from ..models import Question, Answer

def index(request):
    '''
    pybo 목록 출력
    '''
    page = request.GET.get('page','1')
    kw = request.GET.get('kw','')
    so = request.GET.get('so','recent')

    if so == 'recommend' :
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter','-create_date')
    elif so == 'popular' :
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer','-create_date')
    elif so == 'recent' :
        question_list = Question.objects.order_by('-create_date')
    
    #question_list = Question.objects.order_by('-create_date') # - 를 붙임으로 써 역순 정렬

    if kw :
        question_list = question_list.filter(
            Q(subject__icontains=kw) |
            Q(content__icontains=kw) |
            Q(answer__content__icontains=kw) |
            Q(author__username__icontains=kw) |
            Q(answer__author__username__icontains=kw)
        ).distinct()

    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page':page, 'kw':kw, 'so':so}

    return render(request, 'pybo/question_list.html',context)

def detail(request, question_id):
    '''
    pybo 내용 출력
    '''

    page = request.GET.get('page','1')
    so = request.GET.get('so','recent')

    question = get_object_or_404(Question, pk=question_id)
    
    if so == 'recommend' :
        answer_list = Answer.objects.filter(question=question).annotate(num_voter=Count('voter')).order_by('-num_voter','-create_date')
    elif so == 'popular' :
        answer_list = Answer.objects.filter(question=question).annotate(num_comment=Count('comment')).order_by('-num_comment','-create_date')
    elif so == 'recent' :
        answer_list = Answer.objects.filter(question=question).order_by('-create_date')

    answer_list_count = answer_list.count

    paginator = Paginator(answer_list, 10)
    page_obj = paginator.get_page(page)

    context = {'question':question, 'answer_list':page_obj, 'so':so, 'page':page, 'answer_list_count':answer_list_count}
    return render(request, 'pybo/question_detail.html',context)
