from logging import FATAL
from backend.models import KindAnime, User, Kind, Anime, FavoritesKind, FavoritesAnime, Watching, UserRating, Episode
from backend.serializers import AnimeSerializer
from colorama import Fore

def ep_path_builder(anime_name="", anime_season="", ep_number=1, lower_bound=1, upper_bound=10) -> str:
    if anime_name.strip() == "":
        raise ValueError("Anime name must be non-empty string!")
    if not Anime.objects.filter(name=anime_name).exists():
        raise ValueError("Anime name must exist in DB!")
    if not ep_number >= lower_bound and ep_number <= upper_bound:
        raise ValueError("Episode number must lay between bounds!")
    anime_name_uri = anime_name.replace(" ", "")
    if int(ep_number) < 10:
        ep_number = "0" + str(ep_number)
    return f"{anime_name_uri}{anime_season}/{anime_name_uri}{anime_season}_Ep_{ep_number}_SUB_ITA.mp4"

def url_builder(is_https=False, URI="", base_path="", ep_path="") -> str:
    if URI.strip() == "" or ep_path.strip() == "":
        raise ValueError("Both source and episode path fields must be non-empty strings.")
    if "/" not in URI:
        raise ValueError("Invalid source!")
    elif base_path.strip() != "" and "/" not in base_path:
        raise ValueError("Invalid base path!")
    if is_https:
        return f"https://{URI}{base_path}{ep_path}"
    return f"http://{URI}{base_path}{ep_path}"

def episode_filler(MIRROR_URI=None, use_https=False, anime="One Piece", anime_season="", base_path_url="DDL/ANIME/") -> None:
    if not MIRROR_URI:
        raise ValueError(f"{Fore.RED}Mirror URI must exists!")
    queryset = None
    if anime_season.strip() == "":
        queryset = Anime.objects.filter(name=anime)
    else:
        queryset = Anime.objects.filter(name=anime, season=int(anime_season))
    for season in queryset:
        serialized_season = AnimeSerializer(season)
        integrity_check = True
        for j in range(serialized_season.data['start_number_episode'], serialized_season.data['last_episode']+1):
            try:
                ep = Episode(name=str(j),seen=104, e_anime=season, 
                                path=url_builder(is_https=use_https, URI=MIRROR_URI,
                                                base_path=base_path_url,
                                                ep_path=ep_path_builder(
                                                        anime_name=serialized_season.data['name'],
                                                        anime_season=anime_season,
                                                        ep_number=j,
                                                        lower_bound=serialized_season.data['start_number_episode'],
                                                        upper_bound=serialized_season.data['start_number_episode']
                                                )
                                    )           
                        )
                ep.save()
            except ValueError as e:
                print(f"\t{Fore.RED}URL of episode {j} of Anime {serialized_season.data['name']} of season Season {serialized_season.data['season']} is corrupted ---> msg = {str(e)}")
                integrity_check = False
        if integrity_check:
            print(f"{Fore.GREEN}URLs of {serialized_season.data['name']} Season {serialized_season.data['season']} successfully generated!")
        else:
            print(f"{Fore.YELLOW}URLs of {serialized_season.data['name']} Season {serialized_season.data['season']} contain some corrupted URLs!")
    print(f"{Fore.WHITE}Done!")

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
def anime_filler():
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
    a = Anime(name="Boku No Hero Academia", global_rating = 1, plot="x", season=1, last_episode=13, start_number_episode=1, last_update="2016-06-26",autodownlodable=False, finished = True)
    a.save()
    a = Anime(name="Boku No Hero Academia", global_rating = 4, plot="x", season=2, last_episode=25, start_number_episode=0, last_update="2017-09-30",autodownlodable=False, finished = True)
    a.save()
    a = Anime(name="Boku No Hero Academia", global_rating = 3, plot="x", season=3, last_episode=25, start_number_episode=1, last_update="2018-09-29",autodownlodable=False, finished = True)
    a.save()
    a = Anime(name="Boku No Hero Academia", global_rating = 3, plot="x", season=4, last_episode=25, start_number_episode=1, last_update="2020-04-04",autodownlodable=False, finished = True)
    a.save()
    a = Anime(name="Boku No Hero Academia", global_rating = 2, plot="x", season=5, last_episode=11, start_number_episode=1, last_update="2021-06-05",autodownlodable=False, finished = False)
    a.save()
    a = Anime(name="Kuroko No Basket", global_rating = 1, plot="x", season=1, last_episode=25, start_number_episode=1, last_update="2016-06-26",autodownlodable=False, finished = True)
    a.save()
    a = Anime(name="Kuroko No Basket", global_rating = 4, plot="x", season=2, last_episode=25, start_number_episode=0, last_update="2017-09-30",autodownlodable=False, finished = True)
    a.save()
    a = Anime(name="Kuroko No Basket", global_rating = 3, plot="x", season=3, last_episode=25, start_number_episode=1, last_update="2018-09-29",autodownlodable=False, finished = True)
    a.save()
    a = Anime(name="Black Clover", global_rating = 3, plot="x", season=1, last_episode=51, start_number_episode=1, last_update="2018-09-29",autodownlodable=False, finished = True)
    a.save()
    a = Anime(name="Black Clover", global_rating = 3, plot="x", season=2, last_episode=102, start_number_episode=52, last_update="2018-09-29",autodownlodable=False, finished = True)
    a.save()
    a = Anime(name="Black Clover", global_rating = 3, plot="x", season=3, last_episode=154, start_number_episode=103, last_update="2018-09-29",autodownlodable=False, finished = True)
    a.save()
    a = Anime(name="Black Clover", global_rating = 3, plot="x", season=4, last_episode=170, start_number_episode=155, last_update="2018-09-29",autodownlodable=False, finished = True)
    a.save()
ka = KindAnime(ka_anime=Anime.objects.get(name="Boku No Hero Academia", season=1),ka_kind=k)
ka.save()
ka = KindAnime(ka_anime=Anime.objects.get(name="Boku No Hero Academia", season=2),ka_kind=k2)
ka.save()

anime_filler()
episode_filler(MIRROR_URI="www.onlyonepiece.cloud/", anime="One Piece")
episode_filler(MIRROR_URI="www.animeflex.cloud/", anime="Boku No Hero Academia", anime_season="5")
episode_filler(MIRROR_URI="www.brandnewanime.eu/", anime="Kuroko No Basket", anime_season="1")
episode_filler(MIRROR_URI="www.brandnewanime.eu/", anime="Kuroko No Basket", anime_season="2")
episode_filler(MIRROR_URI="www.brandnewanime.eu/", anime="Kuroko No Basket", anime_season="3")
episode_filler(MIRROR_URI="www.animeflex.cloud/", anime="Black Clover", anime_season="1")
episode_filler(MIRROR_URI="www.animeflex.cloud/", anime="Black Clover", anime_season="2")
episode_filler(MIRROR_URI="www.animeflex.cloud/", anime="Black Clover", anime_season="3")
episode_filler(MIRROR_URI="www.animeflex.cloud/", anime="Black Clover", anime_season="4")