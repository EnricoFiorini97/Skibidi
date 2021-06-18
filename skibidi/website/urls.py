from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from website.views import UserCreateView, CustomLogin
from backend.forms import PwdResetForm, PwdChangeForm

urlpatterns = [
        path('',views.index, name='index'),
        path('anime/<str:anime>/<int:stagione>/<int:ep>/',views.anime_ep, name='anime_ep'),
        path('anime/<str:anime>/<int:stagione>/', views.anime_ep_list, name='anime_ep_list'),
        path('signup.html', UserCreateView.as_view()),
        path('forgot-password.html', auth_views.PasswordResetView.as_view(template_name = "registration/forgot-password.html", form_class = PwdResetForm), name ='reset_password'),
        path('reset/password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "registration/passwordreset_sent.html"), name ='password_reset_done'),
        path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = "registration/passwordreset_form.html", form_class=PwdChangeForm), name ='password_reset_confirm'),
        path('reset/password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "registration/passwordreset_done.html"), name ='password_reset_complete'),
        path('admin_control.html', views.admin_control),
        path('login.html', CustomLogin.as_view(), name='login'),
]       