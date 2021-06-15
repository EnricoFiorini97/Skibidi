import env
import json
import requests
from backend.models import Anime, Kind, Episode
from django.shortcuts import render
from django.core.paginator import Paginator
from backend.serializers import KindSerializer, AnimeSerializer, EpisodeSerializer


def kind_inity():
    k_list = []
    querysetKind = Kind.objects.all()
    for q in querysetKind:
        serialized_kind = KindSerializer(q)
        k_list.append(serialized_kind.data["kind_name"])
    return k_list

def index(request):
    query_set = Anime.objects.order_by('name','season')
    paginator = Paginator(query_set, 18)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index-2.html', {'k_list':kind_inity, 'page_obj':page_obj})


def anime_ep(request, anime, stagione, ep):
    querysetAnime = Anime.objects.filter(name=anime, season=stagione)
    for q in querysetAnime:
        if AnimeSerializer(q).data["name"] == anime and AnimeSerializer(q).data["season"] == stagione: 
            identify = AnimeSerializer(q).data['anime_id']
    querysetEpisode = Episode.objects.filter(e_anime=identify, name=str(ep))
    serialized_Episode = EpisodeSerializer(querysetEpisode[0])
    return render(request, 'media.html', {'k_list':kind_inity(), 'query':querysetAnime[0], 'anime': anime,'stagione':stagione,'ep':ep, 'ep_link':serialized_Episode.data["path"]})

def anime_ep_list(request, anime, stagione):
    querysetAnime = Anime.objects.filter(name=anime, season=stagione)
    serialized_Anime = AnimeSerializer(querysetAnime[0])
    return render(request, 'index_episodes.html',{'k_list':kind_inity(), 'anime':anime, 'season':stagione, 'ep_list':range(serialized_Anime.data["start_number_episode"], serialized_Anime.data["last_episode"]+1)})

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def forgot(request):
    return render(request, 'forgot-password.html')

def admin_control(request):
    update_anime = Anime.objects.order_by('name','season')
    update_kind = Kind.objects.all()
    update_episode = Episode.objects.all()
    return render(request, 'admin_control.html', {'update_anime':update_anime, 'update_kind':update_kind, 'update_episode':update_episode})