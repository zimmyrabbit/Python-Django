from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from common.forms import UserForm
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail, BadHeaderError
from django.db.models.query_utils import Q
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

def signup(request):
    '''
    회원가입
    '''

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request,user)
            return redirect('index')
    else :
        form = UserForm()
    return render(request, 'common/signup.html', {'form':form})

def password_reset_request(request):

    '''
    비밀번호 재설정
    '''

    if request.method == 'POST':
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            email = password_reset_form.cleaned_data['email']
            #username = password_reset_form.cleaned_data['username']
            username = request.POST.get('username')
            associated_users = get_user_model().objects.filter(Q(email=email, username=username))
            if associated_users.exists():
                for user in associated_users:
                    subject = 'pybo 비밀번호 찾기'
                    email_template_name = 'common/password_reset_email.txt'
                    c = {
                        'email':user.email,
                        'domain':settings.HOSTNAME,
                        'sitename':'pybo',
                        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                        'user':user,
                        'token':default_token_generator.make_token(user),
                        'protocol':settings.PROTOCOL,
                    }
                    email = render_to_string(email_template_name,c)
                    
                    try:
                        send_mail(subject,email,settings.EMAIL_HOST_USER,[user.email],fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    messages.success(request,'비밀번호 재설정 이메일을 발송했습니다.')
                    return render(request, 'common/password_reset.html')
            else :
                messages.error(request,'해당 사용자를 찾을 수 없습니다.')
                return render(request, 'common/password_reset.html')
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name='common/password_reset.html', context={'password_reset_form':password_reset_form})