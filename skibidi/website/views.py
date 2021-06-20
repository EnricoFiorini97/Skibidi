from django.shortcuts import render
from django.core.paginator import Paginator
from backend.serializers import KindSerializer, AnimeSerializer, EpisodeSerializer
from backend.forms import AuthForm, UserCreateForm, MainForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from backend.models import Kind, Anime, Episode


def kind_inity():
    k_list = []
    querysetKind = Kind.objects.all()
    for q in querysetKind:
        serialized_kind = KindSerializer(q)
        k_list.append(serialized_kind.data["kind_name"])
    return k_list


def index(request):
    form = MainForm()
    if request.GET.get('search') != None:
        query_set = Anime.objects.filter(name__icontains=request.GET.get('search'))
        paginator = Paginator(query_set, len(query_set))
    else:
        query_set = Anime.objects.order_by('name','season')
        paginator = Paginator(query_set, 18)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'form':form, 'kind_list':kind_inity, 'page_obj':page_obj})

def anime_ep(request, anime, stagione, ep):
    querysetAnime = Anime.objects.filter(name=anime, season=stagione)
    for q in querysetAnime:
        if AnimeSerializer(q).data["name"] == anime and AnimeSerializer(q).data["season"] == stagione: 
            identify = AnimeSerializer(q).data['anime_id']
    querysetEpisode = Episode.objects.filter(e_anime=identify, name=str(ep))
    
    Episode.objects.filter(e_anime=identify, name=str(ep)).update(seen=(EpisodeSerializer(querysetEpisode[0])).data['seen']+1)
    
    serialized_Episode = EpisodeSerializer(querysetEpisode[0])
    visual = serialized_Episode.data['seen']
    return render(request, 'media.html', {'kind_list':kind_inity(), 'query':querysetAnime[0], 'anime': anime,'stagione':stagione,'ep':ep, 'ep_link':serialized_Episode.data["path"], 'visual': visual})

def anime_ep_list(request, anime, stagione):
    querysetAnime = Anime.objects.filter(name=anime, season=stagione)
    serialized_Anime = AnimeSerializer(querysetAnime[0])
    return render(request, 'index_episodes.html',{'kind_list':kind_inity(), 'anime':anime, 'season':stagione, 'ep_list':range(serialized_Anime.data["start_number_episode"], serialized_Anime.data["last_episode"]+1)})

def admin_control(request):
    if request.user.is_authenticated and request.user.is_staff:
        update_anime = Anime.objects.order_by('name','season')
        update_kind = Kind.objects.all()
        update_episode = Episode.objects.all()
        return render(request, 'admin_1.html', {'update_anime':update_anime, 'update_kind':update_kind, 'update_episode':update_episode})
    return render(request, 'forbidden.html')

def staff_create(request):
    if request.user.is_authenticated and request.user.is_staff:
        return render(request, 'admin_create.html')
    return render(request, 'forbidden.html')

def staff_update(request):
    if request.user.is_authenticated and request.user.is_staff:
        return render(request, 'admin_update.html')
    return render(request, 'forbidden.html')


def staff_delete(request):
    if request.user.is_authenticated and request.user.is_staff:
        return render(request, 'admin_delete.html')
    return render(request, 'forbidden.html')

class CustomLogin(auth_views.LoginView):
    form_class = AuthForm
    template_name = 'registration/login.html'
    def form_valid(self, form):
        remember = form.cleaned_data['remember_me']
        if not remember:
            self.request.session.set_expiry(604800)
            self.request.session.modified = True
        return super(CustomLogin, self).form_valid(form)


class UserCreateView(CreateView):
    form_class = UserCreateForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('index')
