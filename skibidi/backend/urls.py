from django.urls import path 
from backend import views

urlpatterns = [
        path('search/all/anime/', views.display_all_anime, name="display_all_anime"),
        path('search/anime/<str:anime>/', views.display_anime_by_name, name="display_anime_by_name"),
        path('search/kind/<str:kind>/', views.display_anime_by_kind, name="display_anime_by_kind"),
        path('search/rating/',views.display_anime_by_global_rating, name="display_anime_by_global_rating"),
        path('search/rating/kind/<str:kind>', views.display_anime_by_global_rating_and_kind, name="display_anime_by_global_rating_and_kind"),
        path('search/all/anime/titles/', views.display_all_distinct_titles, name="display_all_distinct_titles"),
        path('search/anime/<str:anime>/seasons', views.display_season_by_anime_name, name="display_season_by_anime_name"),
]