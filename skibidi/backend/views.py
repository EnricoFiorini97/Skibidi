import copy
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from backend.serializers import AnimeSerializer, KindSerializer, FavoritesKindSerializer
from rest_framework import generics, serializers
from backend.models import Anime, Kind, FavoritesKind


class AnimeListAPIView(generics.ListAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer

class KindListAPIView(generics.ListAPIView):
    queryset = Kind.objects.all()
    serializer_class = KindSerializer
    

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