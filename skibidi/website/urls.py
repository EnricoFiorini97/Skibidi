from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from website.views import UserCreateView, CustomLogin

urlpatterns = [
        path('',views.index, name='index'),
        path('anime/<str:anime>/<int:stagione>/<int:ep>/',views.anime_ep, name='anime_ep'),
        path('anime/<str:anime>/<int:stagione>/', views.anime_ep_list, name='anime_ep_list'),
        path('signup.html', UserCreateView.as_view()),
        path('forgot-password.html', views.forgot),
        path('admin_control.html', views.admin_control),
        path('login.html', CustomLogin.as_view(), name='login'),
]       