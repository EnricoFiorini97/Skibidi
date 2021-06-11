import json
import requests
from django.shortcuts import render



def index(request):
    r2 = requests.get('http://127.0.0.1:8000/backend/search/serializers/all/?format=json')
    if r2.status_code == 200:
        print(json.loads(r2.text))
    return render(request, 'index.html', {'anime_list':'capocchione'})


'''
def anime_ep(request, anime, stagione, ep):
    return render(request, 'anime_ep.html', {'anime': anime,'stagione':stagione,'ep':ep})


def anime_ep_list(request, anime, stagione):
    r = json.loads(requests.get(f'http://127.0.0.1:8000/backend/search/anime/{anime}/seasons').text)
    return render(request, 'anime_ep_list.html',{'anime': anime,'stagione':stagione, 'ep_list':range(int(r["body"][stagione-1]["start_number_episode"]),int(r["body"][stagione-1]["last_episode"])+1)})


def anime_seas(request, anime):
    r = json.loads(requests.get(f'http://127.0.0.1:8000/backend/search/anime/{anime}/seasons').text)
    return render(request, 'anime_seas.html',{'anime': anime, 'stagioni': range(len(r["body"]))})'''
