from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("Hello World")
    return render(request, 'index.html')

def anime(request, anime, stagione, ep):
    return render(request, 'anime.html', {'anime': anime,'stagione':stagione,'ep':ep})