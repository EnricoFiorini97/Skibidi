import json
import requests
from django.shortcuts import render

def index(request):
    r = json.loads(requests.get('http://127.0.0.1:8000/backend/search/serializers/anime/all/list').text)
    res = [r[i]['name'] for i in range(len(r))]
    return render(request, 'index.html', {'anime_list':res})

def anime_seas(request, anime):
    r = json.loads(requests.get(f'http://127.0.0.1:8000/backend/search/serializers/anime/{anime}/seasons').text)
    return render(request, 'anime_seas.html',{'anime': anime, 'stagioni': range(len(r))})

def anime_ep(request, anime, stagione, ep):
    print("test")
    return render(request, 'anime_ep.html', {'anime': anime,'stagione':stagione,'ep':ep})

def anime_ep_list(request, anime, stagione):
    r = json.loads(requests.get(f'http://127.0.0.1:8000/backend/search/serializers/anime/{anime}/seasons').text)
    return render(request, 'anime_ep_list.html',{'anime': anime,'stagione':stagione, 'ep_list':range(r[stagione-1]['start_number_episode'], r[stagione-1]['last_episode']+1)})
