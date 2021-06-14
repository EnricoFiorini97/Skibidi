import env
import json
import requests
from backend.models import Anime
from django.shortcuts import render
from django.core.paginator import Paginator

def index(request):
    r = json.loads(requests.get(f'http://{env.MY_IP}:8000/backend/search/serializers/kind/all/').text)
    kind_list = [r[i]['kind_name'] for i in range(len(r))]

    query_set = Anime.objects.order_by('name','season')
    paginator = Paginator(query_set, 18)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index-2.html', {'kind_list':kind_list, 'page_obj':page_obj})


def anime_ep(request, anime, stagione, ep):
    r = json.loads(requests.get(f'http://{env.MY_IP}:8000/backend/search/serializers/anime/all/').text)
    for i in range(len(r)):
        if r[i]["name"] == anime and r[i]['season'] == stagione:
            identify = r[i]['anime_id']        
    r = json.loads(requests.get(f'http://{env.MY_IP}:8000/backend/search/serializers/episodes/anime/{identify}').text)
    if (int(r[0]['name'])) > 1:
        ep_link = r[ep-(int(r[0]['name']))]['path']
    else:
        ep_link = r[ep-1]['path']
    print(ep_link)
    return render(request, 'media.html', {'anime': anime,'stagione':stagione,'ep':ep, 'ep_link':ep_link})

def anime_ep_list(request, anime, stagione):
    r = json.loads(requests.get(f'http://{env.MY_IP}:8000/backend/search/serializers/anime/{anime}/seasons').text)
    return render(request, 'index_episodes.html',{'anime': anime,'stagione':stagione, 'ep_list':range(r[stagione-1]['start_number_episode'], r[stagione-1]['last_episode']+1)})

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def forgot(request):
    return render(request, 'forgot-password.html')