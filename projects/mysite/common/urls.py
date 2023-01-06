from django.urls import path
from django.contrib.auth import views as auth_views

from .views import password_views, profile_views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('signup/',password_views.signup, name='signup'),
    path('password_reset/', password_views.password_reset_request, name="password_reset"),
    #profile
    path('profile/base/<int:user_id>/', profile_views.profile_base, name='profile_base'),
    path('profile/question/<int:user_id>/', profile_views.profile_question, name='profile_question'),
    path('profile/answer/<int:user_id>/', profile_views.profile_answer, name='profile_answer'), 
]