from backend.models import KindAnime, User, Kind, Anime, FavoritesKind, FavoritesAnime, Watching, UserRating, Episode
from backend.serializers import AnimeSerializer

def onepiece_url_generator(ep_number=1) -> str:
    if ep_number < 0:
        raise ValueError("Episode number must be non-negative.")
    str_ep = str(ep_number)
    if ep_number < 10:
        str_ep = "0" + str_ep
    return f"http://www.onlyonepiece.cloud/DDL/ANIME/OnePiece/OnePiece_Ep_{str_ep}_SUB_ITA.mp4"

u = User(username="test", name="name", surname="smith")
u.save()

k = Kind(kind_name="shonen")
k.save()

k2= Kind(kind_name="isekai")
k2.save()

a = Anime(name="Code Geass", global_rating = 5,plot="x", season = 1, last_episode=25, start_number_episode=1, last_update="2021-06-06", autodownlodable=False, finished=False)
a.save()

fk = FavoritesKind(fk_user=u, fk_kind=k)
fk.save()

fa = FavoritesAnime(fa_anime=a, fa_user=u)
fa.save()

e = Episode(name="1", seen=1, e_anime=a, path="")
e.save()

w = Watching(w_user=u, w_anime=a, w_episode=e, seconds=134)
w.save()

ur = UserRating(ur_anime=a,ur_user=u,rating=4)
ur.save()

ka = KindAnime(ka_anime=a,ka_kind=k)
ka.save()

ki = Kind.objects.get(kind_name="shonen")

a = Anime(name="One Piece", global_rating = 5,plot="x", season = 1, last_episode=61, start_number_episode=1, last_update="2021-06-06", autodownlodable=True, finished=True)
a.save()
a = Anime(name="One Piece", global_rating = 1,plot="x", season = 2, last_episode=77, start_number_episode=62, last_update="2021-06-06", autodownlodable=True, finished=True)
a.save()
a = Anime(name="One Piece", global_rating = 3,plot="x", season = 3, last_episode=92, start_number_episode=78, last_update="2021-06-06", autodownlodable=True, finished=True)
a.save()
a = Anime(name="One Piece", global_rating = 5,plot="x", season = 4, last_episode=130, start_number_episode=93, last_update="2021-06-06", autodownlodable=True, finished=True)
a.save()
a = Anime(name="One Piece", global_rating = 4,plot="x", season = 5, last_episode=143, start_number_episode=131, last_update="2021-06-06", autodownlodable=True, finished=True)
a.save()
a = Anime(name="One Piece", global_rating = 1,plot="x", season = 6, last_episode=195, start_number_episode=144, last_update="2021-06-06", autodownlodable=True, finished=True)
a.save()
a = Anime(name="One Piece", global_rating = 2,plot="x", season = 7, last_episode=228, start_number_episode=196, last_update="2021-06-06", autodownlodable=True, finished=True)
a.save()
a = Anime(name="One Piece", global_rating = 4,plot="x", season = 8, last_episode=263, start_number_episode=229, last_update="2021-06-06", autodownlodable=True, finished=True)
a.save()
a = Anime(name="One Piece", global_rating = 1,plot="x", season = 9, last_episode=336, start_number_episode=264, last_update="2021-06-06", autodownlodable=True, finished=True)
a.save()
a = Anime(name="One Piece", global_rating = 2,plot="x", season = 10, last_episode=381, start_number_episode=337, last_update="2021-06-06", autodownlodable=True, finished=True)
a.save()
a = Anime(name="One Piece", global_rating = 2,plot="x", season = 11, last_episode=407, start_number_episode=382, last_update="2021-06-06", autodownlodable=True, finished=True)
a.save()
a = Anime(name="One Piece", global_rating = 5,plot="x", season = 12, last_episode=421, start_number_episode=408, last_update="2021-06-06", autodownlodable=True, finished=True)
a.save()
a = Anime(name="One Piece", global_rating = 4,plot="x", season = 13, last_episode=458, start_number_episode=422, last_update="2021-06-06", autodownlodable=True, finished=True)
a.save()
a = Anime(name="One Piece", global_rating = 3,plot="x", season = 14, last_episode=516, start_number_episode=459, last_update="2021-06-06", autodownlodable=True, finished=True)
a.save()
a = Anime(name="One Piece", global_rating = 2,plot="x", season = 15, last_episode=578, start_number_episode=517, last_update="2021-06-06", autodownlodable=True, finished=True)
a.save()
a = Anime(name="One Piece", global_rating = 1,plot="x", season = 16, last_episode=628, start_number_episode=579, last_update="2021-06-06", autodownlodable=True, finished=True)
a.save()
a = Anime(name="One Piece", global_rating = 5,plot="x", season = 17, last_episode=750, start_number_episode=629, last_update="2021-06-06", autodownlodable=True, finished=True)
a.save()
a = Anime(name="One Piece", global_rating = 4,plot="x", season = 18, last_episode=782, start_number_episode=751, last_update="2021-06-06", autodownlodable=True, finished=True)
a.save()
a = Anime(name="One Piece", global_rating = 5,plot="x", season = 19, last_episode=891, start_number_episode=783, last_update="2021-06-06", autodownlodable=True, finished=True)
a.save()
a = Anime(name="One Piece", global_rating = 5,plot="x", season = 20, last_episode=977, start_number_episode=892, last_update="2021-06-06", autodownlodable=True, finished=False)
a.save()


for season in Anime.objects.filter(name="One Piece"):
    serialized_season = AnimeSerializer(season)
    print(f"Stagione {serialized_season.data['season']} di {serialized_season.data['name']}")
    for j in range(serialized_season.data['start_number_episode'], serialized_season.data['last_episode']+1):
        ep = Episode(name=str(j),seen=104, e_anime=season, path=onepiece_url_generator(ep_number=j))
        ep.save()
        

a.save()
a = Anime(name="My Hero Academia", global_rating = 1, plot="x", season=1, last_episode=13, start_number_episode=1, last_update="2016-06-26",autodownlodable=False, finished = True)
a.save()
a = Anime(name="My Hero Academia", global_rating = 4, plot="x", season=2, last_episode=25, start_number_episode=0, last_update="2017-09-30",autodownlodable=False, finished = True)
a.save()
a = Anime(name="My Hero Academia", global_rating = 3, plot="x", season=3, last_episode=25, start_number_episode=1, last_update="2018-09-29",autodownlodable=False, finished = True)
a.save()
a = Anime(name="My Hero Academia", global_rating = 3, plot="x", season=4, last_episode=25, start_number_episode=1, last_update="2020-04-04",autodownlodable=False, finished = True)
a.save()
a = Anime(name="My Hero Academia", global_rating = 2, plot="x", season=5, last_episode=11, start_number_episode=1, last_update="2021-06-05",autodownlodable=False, finished = False)
a.save()
ka = KindAnime(ka_anime=Anime.objects.get(name="My Hero Academia", season=1),ka_kind=k)
ka.save()
ka = KindAnime(ka_anime=Anime.objects.get(name="My Hero Academia", season=2),ka_kind=k2)
ka.save()



''' nime_id': 1, 'name': 'One Piece', 'plot': 'x', 'season': 1, 'last_episode': 61, 'start_number_episode': 1, 'global_rating': 5, 'path': None, 'last_update': datetime.date(2021, 6, 6), 'autodownlodable': True, 'finished': True}
'''