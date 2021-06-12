import env
import json
import requests
from django.shortcuts import render

def index(request):
    r = json.loads(requests.get(f'http://{env.MY_IP}:8000/backend/search/serializers/anime/all/').text)
    anime_list = {}
    for i in range(len(r)):
        app = {}
        app['name'] = r[i]['name']
        app['season'] = r[i]['season']
        app['rating'] = range(r[i]['global_rating'])
        anime_list[i] = app
    r = json.loads(requests.get(f'http://{env.MY_IP}:8000/backend/search/serializers/kind/all/').text)
    kind_list = [r[i]['kind_name'] for i in range(len(r))]
    return render(request, 'index.html', {'anime_list':anime_list, 'kind_list':kind_list})

def anime_ep(request, anime, stagione, ep):
    print("test")
    return render(request, 'media.html', {'anime': anime,'stagione':stagione,'ep':ep})

def anime_ep_list(request, anime, stagione):
    r = json.loads(requests.get(f'http://{env.MY_IP}:8000/backend/search/serializers/anime/{anime}/seasons').text)
    return render(request, 'index_episodes.html',{'anime': anime,'stagione':stagione, 'ep_list':range(r[stagione-1]['start_number_episode'], r[stagione-1]['last_episode']+1)})

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def forgot(request):
    return render(request, 'forgot-password.html')