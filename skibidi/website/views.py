from django.shortcuts import render
from django.http import HttpResponse
import json


# Create your views here.
def index(request):
    #return HttpResponse("Hello World")
    return render(request, 'index.html')

def anime_ep(request, anime, stagione, ep):
    return render(request, 'anime_ep.html', {'anime': anime,'stagione':stagione,'ep':ep})

def anime_ep_list(request, anime, stagione):
    s = open('/home/zero/Devs/TW/skibidi/anime_list.json','r').read()
    s = json.loads(s)
    return render(request, 'anime_ep_list.html',{'anime': anime,'stagione':stagione, 'ep_list':range(int(s[anime][str(stagione)][0]),int(s[anime][str(stagione)][1])+1)})

def anime_seas(request, anime):
    s = open('/home/zero/Devs/TW/skibidi/anime_list.json','r').read()
    s = json.loads(s)
    print(len(s[anime]))
    return render(request, 'anime_seas.html',{'anime': anime, 'stagioni': range(len(s[anime]))})