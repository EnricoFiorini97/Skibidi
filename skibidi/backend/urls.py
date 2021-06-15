from . import views
from django.urls import path 
from backend.views import AnimeListAPIView, KindListAPIView, UserFavoritesAnimeListAPIView, UserListAPIView, FavoritesKindListAPIView, FavoritesAnimeListAPIView, WatchingListAPIView, UserRatingListAPIView, KindAnimeListAPIView
from backend.views import AnimeUniqueListAPIView, EpisodesListAPIView, SeasonsListAPIView, UserFavoritesKindListAPIView, SpecificAnimeKindListAPIView, AnimeEpisodeListAPIView, KindCreateView, AnimeCreateView, EpisodeCreateView
from backend.views import EpisodeUpdateView, AnimeUpdateView, KindUpdateView, KindDeleteView, AnimeDeleteView, EpisodeDeleteView


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
        path('create/kind/', KindCreateView.as_view()),
        path('create/anime/', AnimeCreateView.as_view()),
        path('create/episode/', EpisodeCreateView.as_view()),
        path('success/', views.success, name='success'),
        path('update/episode/<pk>/', EpisodeUpdateView.as_view()),
        path('update/anime/<pk>/', AnimeUpdateView.as_view()),
        path('update/kind/<pk>/', KindUpdateView.as_view()),
        path('delete/kind/<pk>/', KindDeleteView.as_view()),
        path('delete/anime/<pk>/', AnimeDeleteView.as_view()),
        path('delete/episode/<pk>/', EpisodeDeleteView.as_view()),
]
