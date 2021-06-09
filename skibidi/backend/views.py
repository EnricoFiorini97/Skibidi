from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from . import serializer

@require_http_methods(["GET"])
def display_all_anime(request):
    return HttpResponse(serializer.serialize_all_anime_to_json())


@require_http_methods(["GET"])
def display_anime_by_name(request, anime="One Piece"):
    return HttpResponse(serializer.serialize_anime_by_name_to_json(anime))

