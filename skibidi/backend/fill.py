from backend.models import Anime, FavoritesKind,User, Watching, UserRating, Kind, KindAnime, FavoritesAnime

def fill_user():
    username = input("Inserire username: ")
    name = input("Inserire nome: ")
    surname = input("Inserire cognome: ")
    tmp = User(username=username, name=name, surname=surname)
    tmp.save()

def fill_watching():
    w_user_id = input("Inserire username: ")
    w_anime_id = input("Inserire anime: ")
    episode = input("Inserire episodio: ")
    seconds = input("Inserire secondi: ")

    try:
        tmp = FavoritesKind(w_anime_id = Anime.objects.get(name=w_anime_id), w_user_id = User.objects.get(username=w_user_id), episode = episode, seconds = seconds)
        tmp.save()
    except:
        print("Inserimento non riuscito, anime o username non trovati")

def fill_user_rating():
    ur_anime_id = input("Inserire anime: ")
    ur_user_id = input("Inserire username: ")
    rating = input("Inserire rating: ")

    try:
        tmp = UserRating(ur_anime_id = Anime.objects.get(name=ur_anime_id), ur_user_id = User.objects.get(username=ur_user_id), rating = rating)
        tmp.save()
    except:
        print("Inserimento non riuscito, anime o username non trovati")

def fill_kind():
    kind = input("Inserire genere: ")
    tmp = Kind(kind_name=kind)
    tmp.save()

def fill_kind_anime():
    ka_anime_id = input("Inserire anime: ")
    ka_kind_id = input("Inserire username: ")

    try:
        tmp = UserRating(ka_anime_id = Anime.objects.get(name=ka_anime_id), ka_kind_id = Kind.objects.get(kind_name=ka_kind_id))
        tmp.save()
    except:
        print("Inserimento non riuscito, anime o genere non trovati")

def fill_fav_kind():
    fa_anime_id = input("Inserire anime: ")
    fa_user_id = input("Inserire username: ")
    try:
        tmp = FavoritesAnime(fa_anime_id = Anime.objects.get(name=fa_anime_id), fa_user_id = User.objects.get(username=fa_user_id))
        tmp.save()
    except:
        print("Inserimento non riuscito, anime o username non trovati")

def fill_fav_anime():
    fk_kind_id = input("Inserire genere: ")
    fk_user_id = input("Inserire username: ")
    try:
        tmp = FavoritesKind(fk_kind_id = Kind.objects.get(kind_name=fk_user_id), fk_user_id = User.objects.get(username=fk_user_id))
        tmp.save()
    except:
        print("Inserimento non riuscito, genere o username non trovati")

def fill_anime():
    name = input("Inserire nome dell'anime: ")
    season = input("Inserire stagione: ")
    num_episodes = input("Inserire numero di episodi: ")
    start_number_episode = input("Inserire numero primo episodio: ")
    plot = input("Inserire trama: ")
    path = input("Inserire percorso: ")
    last_update = input("Inserire data ultimo aggiornamento: ")
    autodownlodable = input("Autoscaricabile? (True o False): ")
    finished = input("Finito? (True o False): ")
    tmp = Anime(name=name, season=season, num_episodes=num_episodes, start_number_episode=start_number_episode, plot=plot, path=path, last_update=last_update, autodownlodable=autodownlodable, finished=finished)
    tmp.save()