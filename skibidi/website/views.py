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
    r = json.loads(requests.get(f'http://{env.MY_IP}:8000/backend/search/serializers/anime/all/').text)
    for i in range(len(r)):
        if r[i]["name"] == anime and r[i]['season'] == stagione:
            identify = r[i]['anime_id']        
    r = json.loads(requests.get(f'http://{env.MY_IP}:8000/backend/search/serializers/episodes/anime/{identify}').text)
    return render(request, 'media.html', {'anime': anime,'stagione':stagione,'ep':ep, 'ep_link':r[ep-1]['path']})

def anime_ep_list(request, anime, stagione):
    r = json.loads(requests.get(f'http://{env.MY_IP}:8000/backend/search/serializers/anime/{anime}/seasons').text)
    return render(request, 'index_episodes.html',{'anime': anime,'stagione':stagione, 'ep_list':range(r[stagione-1]['start_number_episode'], r[stagione-1]['last_episode']+1)})

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def forgot(request):
    return render(request, 'forgot-password.html')