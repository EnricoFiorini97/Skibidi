from django.urls import path 
from backend.views import AnimeListAPIView, KindListAPIView, UserFavoritesAnimeListAPIView, UserListAPIView, FavoritesKindListAPIView, FavoritesAnimeListAPIView, WatchingListAPIView, UserRatingListAPIView, KindAnimeListAPIView
from backend.views import AnimeUniqueListAPIView, EpisodesListAPIView, SeasonsListAPIView, UserFavoritesKindListAPIView, SpecificAnimeKindListAPIView, AnimeEpisodeListAPIView


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
        path('search/serializers/favorites/anime/<str:user_id>/', UserFavoritesAnimeListAPIView.as_view()),
        path('search/serializers/favorites/kind/<str:user_id>/', UserFavoritesKindListAPIView.as_view()),
        path('search/serializers/anime/kind/<str:anime_id>/', SpecificAnimeKindListAPIView.as_view()),
        path('search/serializers/episodes/anime/<str:anime_id>/', AnimeEpisodeListAPIView.as_view()),
]
