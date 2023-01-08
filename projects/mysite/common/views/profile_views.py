from itertools import count
from django.shortcuts import render, get_object_or_404

from django.contrib.auth.models import User
from django.db.models import F, Count
from itertools import chain
from pybo.models import Question, Answer, Comment, Category

def profile_base(request, user_id):
    '''
    프로필 기본 정보
    '''
    user = get_object_or_404(User,pk=user_id)
    category_list = Category.objects.all()
    context = {'profile_user':user, 'profile_type':'base', 'category_list':category_list}
    return render(request, 'common/profile/profile_base.html',context)

def profile_question(request, user_id):
    '''
    작성한 게시물
    '''
    user = get_object_or_404(User,pk=user_id)
    category_list = Category.objects.all()
    question = Question.objects.filter(author = user_id)
    context = {'profile_user':user, 'profile_question':question, 'profile_type':'question', 'category_list':category_list}
    return render(request, 'common/profile/profile_question.html',context)

def profile_answer(request, user_id):
    '''
    작성한 답변
    '''
    user = get_object_or_404(User,pk=user_id)
    category_list = Category.objects.all()
    answer = Answer.objects.filter(author = user_id)
    context = {'profile_user':user, 'profile_answer':answer, 'profile_type':'answer', 'category_list':category_list}
    return render(request, 'common/profile/profile_answer.html',context)

def profile_comment(request, user_id):
    '''
    작성한 댓글
    '''
    user = get_object_or_404(User,pk=user_id)
    category_list = Category.objects.all()
    comment = Comment.objects.filter(author = user_id)
    context = {'profile_user':user, 'profile_comment':comment, 'profile_type':'comment', 'category_list':category_list}
    return render(request, 'common/profile/profile_comment.html',context)

def profile_vote(request, user_id):
    '''
    추천한 게시물
    '''
    user = get_object_or_404(User,pk=user_id)
    category_list = Category.objects.all()
    question_list = user.voter_question.annotate(num_voter=Count('voter'))
    answer_list = user.voter_answer.annotate(category=F('question__category__description'), num_voter=Count('voter'))

    _query_set = sorted(
        chain(question_list, answer_list),
        key=lambda obj: obj.create_date,
        reverse=True,
    )

    context = {'profile_user':user, 'profile_vote':_query_set, 'profile_type':'vote', 'category_list':category_list}
    return render(request, 'common/profile/profile_vote.html',context)