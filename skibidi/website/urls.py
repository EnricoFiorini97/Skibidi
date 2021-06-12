from django.urls import path
from . import views

urlpatterns = [
        path('',views.index, name='index'),
        path('anime/<str:anime>/<int:stagione>/<int:ep>/',views.anime_ep, name='anime_ep'),
        path('anime/<str:anime>/<int:stagione>/', views.anime_ep_list, name='anime_ep_list'),
]