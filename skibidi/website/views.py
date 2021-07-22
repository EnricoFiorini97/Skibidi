from django.shortcuts import render
from django.core.paginator import Paginator
from backend.serializers import KindAnimeSerializer, KindSerializer, AnimeSerializer, EpisodeSerializer, UserSerializer, PersonalKindSerializer
from backend.forms import AuthForm, UserCreateForm, MainForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from backend.models import Kind, Anime, Episode, PersonalKind, Watching, KindAnime
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

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
        query_set = Anime.objects.filter(name__icontains=request.GET.get('search')).order_by('name','season')
        paginator = Paginator(query_set, len(query_set))
    else:
        query_set = Anime.objects.order_by('name','season')
        paginator = Paginator(query_set, 18)

    if query_set.exists():
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    else:
        page_obj = {}
    return render(request, 'index.html', {'form':form, 'is_blank':bool(not page_obj) ,'kind_list':kind_inity, 'page_obj':page_obj})

def anime_ep(request, anime, stagione, ep):
    querysetAnime = Anime.objects.filter(name=anime, season=stagione)
    identify = None
    for q in querysetAnime:
        if AnimeSerializer(q).data["name"] == anime and AnimeSerializer(q).data["season"] == stagione: 
            identify = AnimeSerializer(q).data['anime_id']
            
    querysetEpisode = Episode.objects.filter(e_anime=identify, name=str(ep))
    serialized_Episode = None
    try:
        Episode.objects.filter(e_anime=identify, name=str(ep)).update(seen=(EpisodeSerializer(querysetEpisode[0])).data['seen']+1)
        serialized_Episode = EpisodeSerializer(querysetEpisode[0])
    except IndexError:
        return render(request, '404_not_found.html')
    visual = serialized_Episode.data['seen']
    if request.user.is_authenticated: 
        serialized_user_id = UserSerializer(User.objects.filter(username=request.user)[0]).data['id']
        queryset_personal_kind = PersonalKind.objects.filter(p_user=serialized_user_id)

        also_like = set()
        for personal_kind in queryset_personal_kind:
            curr_pk_id = PersonalKindSerializer(personal_kind).data['personal_kind_id']
            for item in KindAnime.objects.filter(ka_kind=curr_pk_id):
                if len(also_like) > 12:
                    break
                tmp = str(item).split(" ")
                anime_name = " ".join(tmp[:-2])
                season = " ".join(tmp[len(tmp)-2:-1])
                also_like.add((anime_name, season))

        try:
            w_user = User.objects.get(username=request.user)
            w_anime = Anime.objects.get(name=anime,season=stagione)
            w_episode = Episode.objects.get(e_anime=identify, name=str(ep))
            w = Watching(w_user=w_user, w_anime=w_anime, w_episode=w_episode)
            w.save()
        except IntegrityError:
            print("[DEBUG] Secondo me è già inserito, poi vedi tu - Cit il DB /[DEBUG]")
            pass
    return render(request, 'media.html', {'kind_list':kind_inity(), 'query':querysetAnime[0], 'anime': anime,'stagione':stagione,'ep':ep, 'ep_link':serialized_Episode.data["path"], 'visual': visual, 'also_like' : also_like})

def anime_ep_list(request, anime, stagione):
    querysetAnime = Anime.objects.filter(name=anime, season=stagione)
    serialized_Anime = AnimeSerializer(querysetAnime[0])
    return render(request, 'index_episodes.html',{'kind_list':kind_inity(), 'anime':anime, 'season':stagione, 'ep_list':range(serialized_Anime.data["start_number_episode"], serialized_Anime.data["last_episode"]+1)})

def profile(request):
    if request.user.is_authenticated:
        user_query = get_user_model().objects.filter(username=request.user)
        personal = PersonalKind.objects.filter(p_user=user_query[0])
        not_like = []
        for k in kind_inity():
            if k not in str(personal):
                not_like.append(k)
        return render(request, 'profile.html', {'kind_list': kind_inity(), 'personal_list':personal, 'not_personal_list':not_like})
    return render(request, 'forbidden.html')

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

def last_watching(request):
    if request.user.is_authenticated:
        w = Watching.objects.filter(w_user=User.objects.get(username=request.user)).order_by('-watching_id')
        arr = []
        for x in w:
            x = str(x)[::-1]
            x = x.split(" ", 2)
            x = [i[::-1] for i in x]
            x[0], x[2] = x[2], x[0]
            arr.append(x)

        try:
            anime = arr[0][0]
            stagione = arr[0][1]
            ep = arr[0][2]
            querysetAnime = Anime.objects.filter(name=anime, season=stagione)
            identify = None

            for q in querysetAnime:
                if AnimeSerializer(q).data["name"] == anime and int(AnimeSerializer(q).data["season"]) == int(stagione):
                    identify = AnimeSerializer(q).data['anime_id']

            querysetEpisode = Episode.objects.filter(e_anime=identify, name=str(ep))
            serialized_Episode = EpisodeSerializer(querysetEpisode[0])
            visual = serialized_Episode.data['seen']

            return render(request, 'history.html', {'kind_list':kind_inity(), 'query':querysetAnime[0], 'anime': anime,'stagione':stagione,'ep':ep, 'ep_link':serialized_Episode.data["path"], 'visual': visual})
        
        except IndexError:
            return render(request, '404_not_found.html')

    return render(request, 'forbidden.html')

def kind_search(request, kind):
    identify = None
    querysetKind = Kind.objects.filter(kind_name=kind)

    for q in querysetKind:
        if KindSerializer(q).data["kind_name"] == kind:
            identify = KindSerializer(q).data["kind_id"]
    
    querysetKindAnime = KindAnime.objects.filter(ka_kind=identify)
    tmp = []
    for q in querysetKindAnime:
        tmp.append(str(q)[:-len(kind)-1].rsplit(" ", 1))

    return render(request, 'kind.html', {'anime_list':tmp, 'kind_list':kind_inity(), 'kind':kind})
