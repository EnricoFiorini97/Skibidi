from . import views
from django.urls import path 
from backend.views import AnimeListAPIView, KindListAPIView, UserFavoritesAnimeListAPIView, UserListAPIView, FavoritesKindListAPIView, FavoritesAnimeListAPIView, WatchingListAPIView, UserRatingListAPIView, KindAnimeListAPIView
from backend.views import AnimeUniqueListAPIView, EpisodesListAPIView, SeasonsListAPIView, UserFavoritesKindListAPIView, SpecificAnimeKindListAPIView, AnimeEpisodeListAPIView
from backend.views import WatchingCreateView, KindCreateView, AnimeCreateView, EpisodeCreateView, FavoritesAnimeCreateView, RoleCreateView, UserCreateView, FavoritesKindCreateView, UserRatingCreateView, KindAnimeCreateView
from backend.views import KindAnimeUpdateView, EpisodeUpdateView, AnimeUpdateView, KindUpdateView, WatchingUpdateView, UserRatingUpdateView, FavoritesAnimeUpdateView, FavoritesKindUpdateView, RoleUpdateView, UserUpdateView
from backend.views import KindAnimeDeleteView, EpisodeDeleteView, AnimeDeleteView, KindDeleteView, WatchingDeleteView, UserRatingDeleteView, FavoritesAnimeDeleteView, FavoritesKindDeleteView, RoleDeleteView, UserDeleteView
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
        # ---- From Here ----
        path('success/', views.success, name='success'),
        # ---- Create ----
        path('create/kind/', KindCreateView.as_view()),
        path('create/anime/', AnimeCreateView.as_view()),
        path('create/episode/', EpisodeCreateView.as_view()),
        path('create/favorites/anime/', FavoritesAnimeCreateView.as_view()),
        path('create/role/', RoleCreateView.as_view()),
        path('create/user/', UserCreateView.as_view()),
        path('create/favorites/kind/', FavoritesKindCreateView.as_view()),
        path('create/kind/anime/', KindAnimeCreateView.as_view()),
        path('create/user/rating/', UserRatingCreateView.as_view()),
        path('create/watching/', WatchingCreateView.as_view()),
        # ---- Update ----
        path('update/episode/<pk>/', EpisodeUpdateView.as_view()),
        path('update/anime/<pk>/', AnimeUpdateView.as_view()),
        path('update/kind/<int:pk>/', KindUpdateView.as_view()),
        path('update/favorites/anime/<pk>/', FavoritesAnimeUpdateView.as_view()),
        path('update/role/<pk>/', RoleUpdateView.as_view()),
        path('update/user/<pk>/', UserUpdateView.as_view()),
        path('update/favorites/kind/<pk>/', FavoritesKindUpdateView.as_view()),
        path('update/kind/anime/<pk>/', KindAnimeUpdateView.as_view()),
        path('update/user/rating/<pk>/', UserRatingUpdateView.as_view()),
        path('update/watching/<pk>/', WatchingUpdateView.as_view()),
        # ---- Delete ----
        path('delete/kind/<pk>/', KindDeleteView.as_view()),
        path('delete/anime/<pk>/', AnimeDeleteView.as_view()),
        path('delete/episode/<pk>/', EpisodeDeleteView.as_view()),
        path('delete/favorites/anime/<pk>/', FavoritesAnimeDeleteView.as_view()),
        path('delete/role/<pk>/', RoleDeleteView.as_view()),
        path('delete/user/<pk>/', UserDeleteView.as_view()),
        path('delete/favorites/kind/<pk>/', FavoritesKindDeleteView.as_view()),
        path('delete/kind/anime/<pk>/', KindAnimeDeleteView.as_view()),
        path('delete/user/rating/<pk>/', UserRatingDeleteView.as_view()),
        path('delete/watching/<pk>/', WatchingDeleteView.as_view()),
]
