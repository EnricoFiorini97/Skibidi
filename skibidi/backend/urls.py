from django.urls import path 
from backend import views

urlpatterns = [
        path('search/all/anime/', views.display_all_anime, name="display_all_anime"),
        path('search/anime/<str:anime>/', views.display_anime_by_name, name="display_anime_by_name"),
]