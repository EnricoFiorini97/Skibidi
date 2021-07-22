from . import views
from django.urls import path 
from backend.views import AnimeListAPIView, KindListAPIView, UserListAPIView, WatchingListAPIView, KindAnimeListAPIView
from backend.views import AnimeUniqueListAPIView, EpisodesListAPIView, SeasonsListAPIView, SpecificAnimeKindListAPIView, AnimeEpisodeListAPIView
from backend.views import PersonalKindCreateView, WatchingCreateView, KindCreateView, AnimeCreateView, EpisodeCreateView, UserCreateView, KindAnimeCreateView
from backend.views import PersonalKindUpdateView, KindAnimeUpdateView, EpisodeUpdateView, AnimeUpdateView, KindUpdateView, WatchingUpdateView, UserUpdateView
from backend.views import PersonalKindDeleteView, KindAnimeDeleteView, EpisodeDeleteView, AnimeDeleteView, KindDeleteView, WatchingDeleteView, UserDeleteView


urlpatterns = [
        path('search/serializers/anime/all/', AnimeListAPIView.as_view()),
        path('search/serializers/kind/all/', KindListAPIView.as_view()),
        path('search/serializers/user/all/', UserListAPIView.as_view()),
        path('search/serializers/watching/all/', WatchingListAPIView.as_view()),
        path('search/serializers/kind/anime/all/', KindAnimeListAPIView.as_view()),
        path('search/serializers/anime/all/list/', AnimeUniqueListAPIView.as_view()),
        path('search/serializers/anime/<str:anime>/seasons/', SeasonsListAPIView.as_view()),
        path('search/serializers/anime/<str:anime>/<int:season>/episodes/', EpisodesListAPIView.as_view()),
        path('search/serializers/anime/kind/<str:anime_id>/', SpecificAnimeKindListAPIView.as_view()),
        path('search/serializers/episodes/anime/<str:anime_id>/', AnimeEpisodeListAPIView.as_view()),
        # ---- From Here ----
        path('success/', views.success, name='success'),
        # ---- Create ----
        path('create/kind/', KindCreateView.as_view()),
        path('create/anime/', AnimeCreateView.as_view()),
        path('create/episode/', EpisodeCreateView.as_view()),
        path('create/user/', UserCreateView.as_view()),
        path('create/kind/anime/', KindAnimeCreateView.as_view()),
        path('create/watching/', WatchingCreateView.as_view()),
        path('create/personal/kind/', PersonalKindCreateView.as_view()),
        # ---- Update ----
        path('update/episode/<pk>/', EpisodeUpdateView.as_view()),
        path('update/anime/<pk>/', AnimeUpdateView.as_view()),
        path('update/kind/<pk>/', KindUpdateView.as_view()),
        path('update/user/<pk>/', UserUpdateView.as_view()),
        path('update/kind/anime/<pk>/', KindAnimeUpdateView.as_view()),
        path('update/watching/<pk>/', WatchingUpdateView.as_view()),
        path('update/personal/kind/<pk>/', PersonalKindUpdateView.as_view()),
        # ---- Delete ----
        path('delete/kind/<pk>/', KindDeleteView.as_view()),
        path('delete/anime/<pk>/', AnimeDeleteView.as_view()),
        path('delete/episode/<pk>/', EpisodeDeleteView.as_view()),
        path('delete/user/<pk>/', UserDeleteView.as_view()),
        path('delete/kind/anime/<pk>/', KindAnimeDeleteView.as_view()),
        path('delete/watching/<pk>/', WatchingDeleteView.as_view()),
        path('delete/personal/kind/<pk>/', PersonalKindDeleteView.as_view()),
        path('create/personal/<str:kind>/<str:user>/', views.add_personal),
        path('delete/personal/<str:kind>/<str:user>/', views.del_personal),
]
