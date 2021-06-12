import copy
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from backend.serializers import AnimeSerializer, KindSerializer, FavoritesKindSerializer, UserRatingSerializer, WatchingSerializer, FavoritesAnimeSerializer, KindAnimeSerializer, UserSerializer
from rest_framework import generics, serializers
from backend.models import Anime, Kind, FavoritesKind, UserRating, Watching, FavoritesAnime, KindAnime, User


class AnimeListAPIView(generics.ListAPIView):
    queryset = Anime.objects.order_by('name','season')
    serializer_class = AnimeSerializer


class AnimeUniqueListAPIView(generics.ListAPIView):
    queryset = Anime.objects.filter(season=1)
    serializer_class = AnimeSerializer


class SeasonsListAPIView(generics.ListAPIView):
    serializer_class = AnimeSerializer
    
    def get_queryset(self):
        name= self.kwargs['anime']
        tmp = Anime.objects.filter(name=name)
        return tmp


class EpisodesListAPIView(generics.ListAPIView):
    serializer_class = AnimeSerializer
    
    def get_queryset(self):
        name = self.kwargs['anime']
        season = self.kwargs['season']
        tmp = Anime.objects.filter(name=name, season=season)
        return tmp
    

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



'''
@require_http_methods(["GET"])
def display_all_anime(request):
    return HttpResponse(serializers.serialize_all_anime_to_json())


@require_http_methods(["GET"])
def display_anime_by_name(request, anime="One Piece"):
    return HttpResponse(serializers.serialize_anime_by_name_to_json(anime))


@require_http_methods(["GET"])
def display_anime_by_kind(request, kind="shonen"):
    return HttpResponse(serializers.serialize_anime_by_kind_to_json(kind))


@require_http_methods(["GET"])
def display_anime_by_global_rating(request):
    return HttpResponse(serializers.serialize_anime_by_global_rating_to_json())


@require_http_methods(["GET"])
def display_anime_by_global_rating_and_kind(request, kind="shonen"):
    return HttpResponse(serializers.serialize_anime_by_global_rating_and_kind_to_json(kind))


@require_http_methods(["GET"])
def display_all_distinct_titles(request):
    return HttpResponse(serializers.serialize_all_distinct_titles_to_json())
    s

@require_http_methods(["GET"])
def display_season_by_anime_name(request, anime="One Piece"):
    return HttpResponse(serializers.serialize_season_by_anime_name_to_json(anime))'''