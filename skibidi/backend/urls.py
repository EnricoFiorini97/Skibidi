from django.urls import path 
from backend import views
from backend.views import AnimeListAPIView, KindListAPIView, UserListAPIView, FavoritesKindListAPIView, FavoritesAnimeListAPIView, WatchingListAPIView, UserRatingListAPIView, KindAnimeListAPIView
from backend.views import AnimeUniqueListAPIView, EpisodesListAPIView, SeasonsListAPIView
from backend import views

urlpatterns = [
        path('search/serializers/anime/all/', AnimeListAPIView.as_view()),
        path('search/serializers/kind/all/', KindListAPIView.as_view()),
        path('search/serializers/user/all/', UserListAPIView.as_view()),
        path('search/serializers/favorites/kind/all/', FavoritesKindListAPIView.as_view()),
        path('search/serializers/favorites/anime/all/', FavoritesAnimeListAPIView.as_view()),
        path('search/serializers/watching/all/', WatchingListAPIView.as_view()),
        path('search/serializers/user/rating/all/', UserRatingListAPIView.as_view()),
        path('search/serializers/kind/anime/all/', KindAnimeListAPIView.as_view()),
        path('search/serializers/anime/all/list/', AnimeUniqueListAPIView.as_view()),
        path('search/serializers/anime/<str:anime>/seasons/', SeasonsListAPIView.as_view()),
        path('search/serializers/anime/<str:anime>/<int:season>/episodes/', EpisodesListAPIView.as_view()),
]
