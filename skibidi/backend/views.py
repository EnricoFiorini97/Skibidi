from backend.serializers import AnimeSerializer, KindSerializer, FavoritesKindSerializer, UserRatingSerializer, WatchingSerializer, FavoritesAnimeSerializer, KindAnimeSerializer, UserSerializer, EpisodeSerializer
from rest_framework import generics
from backend.models import Anime, Episode, Kind, FavoritesKind, UserRating, Watching, FavoritesAnime, KindAnime, User

from django.views.generic.edit import CreateView
from .forms import KindForm, AnimeForm, EpisodeForm
from django.urls import reverse

class AnimeListAPIView(generics.ListAPIView):
    queryset = Anime.objects.order_by('name','season')
    serializer_class = AnimeSerializer


class AnimeUniqueListAPIView(generics.ListAPIView):
    queryset = Anime.objects.filter(season=1)
    serializer_class = AnimeSerializer


class SeasonsListAPIView(generics.ListAPIView):
    serializer_class = AnimeSerializer
    
    def get_queryset(self):
        return Anime.objects.filter(name=self.kwargs['anime'])


class EpisodesListAPIView(generics.ListAPIView):
    serializer_class = AnimeSerializer
    
    def get_queryset(self):
        return Anime.objects.filter(name=self.kwargs['anime'], season=self.kwargs['season'])
 
    
class KindListAPIView(generics.ListAPIView):
    queryset = Kind.objects.all()
    serializer_class = KindSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FavoritesKindListAPIView(generics.ListAPIView):
    queryset = FavoritesKind.objects.all()
    serializer_class = FavoritesKindSerializer


class FavoritesAnimeListAPIView(generics.ListAPIView):
    queryset = FavoritesAnime.objects.all()
    serializer_class = FavoritesAnimeSerializer


class WatchingListAPIView(generics.ListAPIView):
    queryset = Watching.objects.all()
    serializer_class = WatchingSerializer


class UserRatingListAPIView(generics.ListAPIView):
    queryset = UserRating.objects.all()
    serializer_class = UserRatingSerializer


class KindAnimeListAPIView(generics.ListAPIView):
    queryset = KindAnime.objects.all()
    serializer_class = KindAnimeSerializer


class UserFavoritesAnimeListAPIView(generics.ListAPIView):
    serializer_class = FavoritesAnimeSerializer
    
    def get_queryset(self):
        return FavoritesAnime.objects.filter(fa_user_id=self.kwargs['user_id'])


class UserFavoritesKindListAPIView(generics.ListAPIView):
    serializer_class = FavoritesKindSerializer
    
    def get_queryset(self):
        return FavoritesKind.objects.filter(fk_user_id=self.kwargs['user_id'])


class SpecificAnimeKindListAPIView(generics.ListAPIView):
    serializer_class = KindAnimeSerializer
    
    def get_queryset(self):
        return KindAnime.objects.filter(ka_anime_id=self.kwargs['anime_id'])


class AnimeEpisodeListAPIView(generics.ListAPIView):
    serializer_class = EpisodeSerializer

    def get_queryset(self):
        return Episode.objects.filter(e_anime=self.kwargs['anime_id'])

class KindCreateView(CreateView): 
    form_class = KindForm
    model = Kind
    template_name="form.html"

    def get_success_url(self):
        return reverse('index')


class AnimeCreateView(CreateView):
    form_class = AnimeForm
    model = Anime
    template_name = "form.html"

    def get_success_url(self):
        return reverse('index')

class AnimeCreateView(CreateView):
    form_class = EpisodeForm
    model = Episode
    template_name = "form.html"

    def get_success_url(self):
        return reverse('index')
