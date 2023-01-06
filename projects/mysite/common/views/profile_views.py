from django.shortcuts import render, get_object_or_404

from django.contrib.auth.models import User
from pybo.models import Question, Answer

def profile_base(request, user_id):
    '''
    프로필 기본 정보
    '''
    user = get_object_or_404(User,pk=user_id)
    context = {'profile_user':user, 'profile_type':'base'}
    return render(request, 'common/profile/profile_base.html',context)

def profile_question(request, user_id):
    '''
    작성한 게시물
    '''
    user = get_object_or_404(User,pk=user_id)
    question = Question.objects.filter(author = user_id)
    context = {'profile_user':user, 'profile_question':question, 'profile_type':'question'}
    return render(request, 'common/profile/profile_question.html',context)

def profile_answer(request, user_id):
    '''
    작성한 답변
    '''
    user = get_object_or_404(User,pk=user_id)
    answer = Answer.objects.filter(author = user_id)
    context = {'profile_user':user, 'profile_answer':answer, 'profile_type':'answer'}
    return render(request, 'common/profile/profile_answer.html',context)