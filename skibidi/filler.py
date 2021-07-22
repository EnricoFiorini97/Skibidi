from backend.models import KindAnime, User, Kind, Anime, Watching, Episode
from backend.serializers import AnimeSerializer
from colorama import Fore
from django.contrib.auth.models import User

def img_source_builder(name="One Piece", season="1") -> str:
    return f"static/img/Anime/{name} {season}.jpg"

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



u = User.objects.create_user(first_name="Enrico", last_name="Fiorini", email="test@gmail.com", username="enrico", password="pass", is_staff=True)
u.save()

u = User.objects.create_user(first_name="Carmine", last_name="la Luna", email="test2@gmail.com", username="carmine", password="pass", is_staff=True)
u.save()

u = User.objects.create_user(first_name="Unprivileged", last_name="Customer", email="test3@gmail.com", username="unprivileged", password="pass")
u.save()

k = Kind(kind_name="shonen")
k.save()

k2= Kind(kind_name="isekai")
k2.save()

a = Anime(name="Code Geass", global_rating = 5,plot="x", season="1", last_episode=25, start_number_episode=1, last_update="2021-06-06", autodownlodable=False, finished=False, img_source=img_source_builder(name="Code Geass", season="1"))
a.save()

a = Anime(name="Code Geass", global_rating = 5,plot="x", season="2", last_episode=25, start_number_episode=1, last_update="2021-06-06", autodownlodable=False, finished=False, img_source=img_source_builder(name="Code Geass", season="2"))
a.save()

e = Episode(name="1", seen=1, e_anime=a, path="")
e.save()

w = Watching(w_user=u, w_anime=a, w_episode=e, seconds=134)
w.save()

ka = KindAnime(ka_anime=a,ka_kind=k)
ka.save()

ki = Kind.objects.get(kind_name="shonen")

a = Anime(name="One Piece", global_rating = 5,plot="x", season = 1, last_episode=61, start_number_episode=1, last_update="2021-06-06", autodownlodable=True, finished=True, img_source=img_source_builder(name="One Piece", season="1"))
a.save()
a = Anime(name="One Piece", global_rating = 1,plot="x", season = 2, last_episode=77, start_number_episode=62, last_update="2021-06-06", autodownlodable=True, finished=True, img_source=img_source_builder(name="One Piece", season="2"))
a.save()
a = Anime(name="One Piece", global_rating = 3,plot="x", season = 3, last_episode=92, start_number_episode=78, last_update="2021-06-06", autodownlodable=True, finished=True, img_source=img_source_builder(name="One Piece", season="3"))
a.save()
a = Anime(name="One Piece", global_rating = 5,plot="x", season = 4, last_episode=130, start_number_episode=93, last_update="2021-06-06", autodownlodable=True, finished=True, img_source=img_source_builder(name="One Piece", season="4"))
a.save()
a = Anime(name="One Piece", global_rating = 4,plot="x", season = 5, last_episode=143, start_number_episode=131, last_update="2021-06-06", autodownlodable=True, finished=True, img_source=img_source_builder(name="One Piece", season="5"))
a.save()
a = Anime(name="One Piece", global_rating = 1,plot="x", season = 6, last_episode=195, start_number_episode=144, last_update="2021-06-06", autodownlodable=True, finished=True, img_source=img_source_builder(name="One Piece", season="6"))
a.save()
a = Anime(name="One Piece", global_rating = 2,plot="x", season = 7, last_episode=228, start_number_episode=196, last_update="2021-06-06", autodownlodable=True, finished=True, img_source=img_source_builder(name="One Piece", season="7"))
a.save()
a = Anime(name="One Piece", global_rating = 4,plot="x", season = 8, last_episode=263, start_number_episode=229, last_update="2021-06-06", autodownlodable=True, finished=True, img_source=img_source_builder(name="One Piece", season="8"))
a.save()
a = Anime(name="One Piece", global_rating = 1,plot="x", season = 9, last_episode=336, start_number_episode=264, last_update="2021-06-06", autodownlodable=True, finished=True, img_source=img_source_builder(name="One Piece", season="9"))
a.save()
a = Anime(name="One Piece", global_rating = 2,plot="x", season = 10, last_episode=381, start_number_episode=337, last_update="2021-06-06", autodownlodable=True, finished=True, img_source=img_source_builder(name="One Piece", season="10"))
a.save()
a = Anime(name="One Piece", global_rating = 2,plot="x", season = 11, last_episode=407, start_number_episode=382, last_update="2021-06-06", autodownlodable=True, finished=True, img_source=img_source_builder(name="One Piece", season="11"))
a.save()
a = Anime(name="One Piece", global_rating = 5,plot="x", season = 12, last_episode=421, start_number_episode=408, last_update="2021-06-06", autodownlodable=True, finished=True, img_source=img_source_builder(name="One Piece", season="12"))
a.save()
a = Anime(name="One Piece", global_rating = 4,plot="x", season = 13, last_episode=458, start_number_episode=422, last_update="2021-06-06", autodownlodable=True, finished=True, img_source=img_source_builder(name="One Piece", season="13"))
a.save()
a = Anime(name="One Piece", global_rating = 3,plot="x", season = 14, last_episode=516, start_number_episode=459, last_update="2021-06-06", autodownlodable=True, finished=True, img_source=img_source_builder(name="One Piece", season="14"))
a.save()
a = Anime(name="One Piece", global_rating = 2,plot="x", season = 15, last_episode=578, start_number_episode=517, last_update="2021-06-06", autodownlodable=True, finished=True, img_source=img_source_builder(name="One Piece", season="15"))
a.save()
a = Anime(name="One Piece", global_rating = 1,plot="x", season = 16, last_episode=628, start_number_episode=579, last_update="2021-06-06", autodownlodable=True, finished=True, img_source=img_source_builder(name="One Piece", season="16"))
a.save()
a = Anime(name="One Piece", global_rating = 5,plot="x", season = 17, last_episode=750, start_number_episode=629, last_update="2021-06-06", autodownlodable=True, finished=True, img_source=img_source_builder(name="One Piece", season="17"))
a.save()
a = Anime(name="One Piece", global_rating = 4,plot="x", season = 18, last_episode=782, start_number_episode=751, last_update="2021-06-06", autodownlodable=True, finished=True, img_source=img_source_builder(name="One Piece", season="18"))
a.save()
a = Anime(name="One Piece", global_rating = 5,plot="x", season = 19, last_episode=891, start_number_episode=783, last_update="2021-06-06", autodownlodable=True, finished=True, img_source=img_source_builder(name="One Piece", season="19"))
a.save()
a = Anime(name="One Piece", global_rating = 5,plot="x", season = 20, last_episode=977, start_number_episode=892, last_update="2021-06-06", autodownlodable=True, finished=False, img_source=img_source_builder(name="One Piece", season="20"))
a.save()
a = Anime(name="Boku No Hero Academia", global_rating = 1, plot="x", season=1, last_episode=13, start_number_episode=1, last_update="2016-06-26",autodownlodable=False, finished=True, img_source=img_source_builder(name="Boku No Hero Academia", season="1"))
a.save()
a = Anime(name="Boku No Hero Academia", global_rating = 4, plot="x", season=2, last_episode=25, start_number_episode=0, last_update="2017-09-30",autodownlodable=False, finished=True, img_source=img_source_builder(name="Boku No Hero Academia", season="2"))
a.save()
a = Anime(name="Boku No Hero Academia", global_rating = 3, plot="x", season=3, last_episode=25, start_number_episode=1, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="Boku No Hero Academia", season="3"))
a.save()
a = Anime(name="Boku No Hero Academia", global_rating = 3, plot="x", season=4, last_episode=25, start_number_episode=1, last_update="2020-04-04",autodownlodable=False, finished=True, img_source=img_source_builder(name="Boku No Hero Academia", season="4"))
a.save()
a = Anime(name="Boku No Hero Academia", global_rating = 2, plot="x", season=5, last_episode=11, start_number_episode=1, last_update="2021-06-05",autodownlodable=False, finished=False, img_source=img_source_builder(name="Boku No Hero Academia", season="5"))
a.save()
a = Anime(name="Kuroko No Basket", global_rating = 1, plot="x", season=1, last_episode=25, start_number_episode=1, last_update="2016-06-26",autodownlodable=False, finished=True, img_source=img_source_builder(name="Kuroko No Basket", season="1"))
a.save()
a = Anime(name="Kuroko No Basket", global_rating = 4, plot="x", season=2, last_episode=25, start_number_episode=0, last_update="2017-09-30",autodownlodable=False, finished=True, img_source=img_source_builder(name="Kuroko No Basket", season="2"))
a.save()
a = Anime(name="Kuroko No Basket", global_rating = 3, plot="x", season=3, last_episode=25, start_number_episode=1, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="Kuroko No Basket", season="3"))
a.save()
a = Anime(name="Black Clover", global_rating = 3, plot="x", season=1, last_episode=51, start_number_episode=1, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="Black Clover", season="1"))
a.save()
a = Anime(name="Black Clover", global_rating = 3, plot="x", season=2, last_episode=102, start_number_episode=52, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="Black Clover", season="2"))
a.save()
a = Anime(name="Black Clover", global_rating = 3, plot="x", season=3, last_episode=154, start_number_episode=103, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="Black Clover", season="3"))
a.save()
a = Anime(name="Black Clover", global_rating = 3, plot="x", season=4, last_episode=170, start_number_episode=155, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="Black Clover", season="4"))
a.save()
a = Anime(name="Naruto", global_rating = 3, plot="x", season=1, last_episode=35, start_number_episode=1, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="Naruto", season="1"))
a.save()
a = Anime(name="Naruto", global_rating = 3, plot="x", season=2, last_episode=83, start_number_episode=36, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="Naruto", season="2"))
a.save()
a = Anime(name="Naruto", global_rating = 3, plot="x", season=3, last_episode=131, start_number_episode=84, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="Naruto", season="3"))
a.save()
a = Anime(name="Naruto", global_rating = 3, plot="x", season=4, last_episode=185, start_number_episode=134, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="Naruto", season="4"))
a.save()
a = Anime(name="Naruto", global_rating = 3, plot="x", season=5, last_episode=225, start_number_episode=186, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="Naruto", season="5"))
a.save()
a = Anime(name="NarutoShippuden", global_rating = 3, plot="x", season=1, last_episode=32, start_number_episode=1, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="NarutoShippuden", season="1"))
a.save()
a = Anime(name="NarutoShippuden", global_rating = 3, plot="x", season=2, last_episode=53, start_number_episode=33, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="NarutoShippuden", season="2"))
a.save()
a = Anime(name="NarutoShippuden", global_rating = 3, plot="x", season=3, last_episode=71, start_number_episode=54, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="NarutoShippuden", season="3"))
a.save()
a = Anime(name="NarutoShippuden", global_rating = 3, plot="x", season=4, last_episode=88, start_number_episode=72, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="NarutoShippuden", season="4"))
a.save()
a = Anime(name="NarutoShippuden", global_rating = 3, plot="x", season=5, last_episode=112, start_number_episode=89, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="NarutoShippuden", season="5"))
a.save()
a = Anime(name="NarutoShippuden", global_rating = 3, plot="x", season=6, last_episode=143, start_number_episode=113, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="NarutoShippuden", season="6"))
a.save()
a = Anime(name="NarutoShippuden", global_rating = 3, plot="x", season=7, last_episode=151, start_number_episode=144, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="NarutoShippuden", season="7"))
a.save()
a = Anime(name="NarutoShippuden", global_rating = 3, plot="x", season=8, last_episode=175, start_number_episode=152, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="NarutoShippuden", season="8"))
a.save()
a = Anime(name="NarutoShippuden", global_rating = 3, plot="x", season=9, last_episode=196, start_number_episode=176, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="NarutoShippuden", season="9"))
a.save()
a = Anime(name="NarutoShippuden", global_rating = 3, plot="x", season=10, last_episode=221, start_number_episode=197, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="NarutoShippuden", season="10"))
a.save()

a = Anime(name="NarutoShippuden", global_rating = 3, plot="x", season=11, last_episode=242, start_number_episode=222, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="NarutoShippuden", season="11"))
a.save()
a = Anime(name="NarutoShippuden", global_rating = 3, plot="x", season=12, last_episode=275, start_number_episode=243, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="NarutoShippuden", season="12"))
a.save()
a = Anime(name="NarutoShippuden", global_rating = 3, plot="x", season=13, last_episode=289, start_number_episode=276, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="NarutoShippuden", season="13"))
a.save()
a = Anime(name="NarutoShippuden", global_rating = 3, plot="x", season=14, last_episode=295, start_number_episode=290, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="NarutoShippuden", season="14"))
a.save()
a = Anime(name="NarutoShippuden", global_rating = 3, plot="x", season=15, last_episode=320, start_number_episode=296, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="NarutoShippuden", season="15"))
a.save()
a = Anime(name="NarutoShippuden", global_rating = 3, plot="x", season=16, last_episode=348, start_number_episode=321, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="NarutoShippuden", season="16"))
a.save()
a = Anime(name="NarutoShippuden", global_rating = 3, plot="x", season=17, last_episode=361, start_number_episode=349, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="NarutoShippuden", season="17"))
a.save()
a = Anime(name="NarutoShippuden", global_rating = 3, plot="x", season=18, last_episode=372, start_number_episode=362, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="NarutoShippuden", season="18"))
a.save()
a = Anime(name="NarutoShippuden", global_rating = 3, plot="x", season=19, last_episode=393, start_number_episode=373, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="NarutoShippuden", season="19"))
a.save()
a = Anime(name="NarutoShippuden", global_rating = 3, plot="x", season=20, last_episode=413, start_number_episode=394, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="NarutoShippuden", season="20"))
a.save()

a = Anime(name="NarutoShippuden", global_rating = 3, plot="x", season=21, last_episode=431, start_number_episode=414, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="NarutoShippuden", season="21"))
a.save()
a = Anime(name="NarutoShippuden", global_rating = 3, plot="x", season=22, last_episode=450, start_number_episode=432, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="NarutoShippuden", season="22"))
a.save()
a = Anime(name="NarutoShippuden", global_rating = 3, plot="x", season=23, last_episode=458, start_number_episode=451, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="NarutoShippuden", season="23"))
a.save()
a = Anime(name="NarutoShippuden", global_rating = 3, plot="x", season=24, last_episode=469, start_number_episode=459, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="NarutoShippuden", season="24"))
a.save()
a = Anime(name="NarutoShippuden", global_rating = 3, plot="x", season=25, last_episode=479, start_number_episode=470, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="NarutoShippuden", season="25"))
a.save()
a = Anime(name="NarutoShippuden", global_rating = 3, plot="x", season=26, last_episode=483, start_number_episode=480, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="NarutoShippuden", season="26"))
a.save()
a = Anime(name="NarutoShippuden", global_rating = 3, plot="x", season=27, last_episode=488, start_number_episode=484, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="NarutoShippuden", season="27"))
a.save()
a = Anime(name="NarutoShippuden", global_rating = 3, plot="x", season=28, last_episode=493, start_number_episode=489, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="NarutoShippuden", season="28"))
a.save()
a = Anime(name="NarutoShippuden", global_rating = 3, plot="x", season=29, last_episode=500, start_number_episode=494, last_update="2018-09-29",autodownlodable=False, finished=True, img_source=img_source_builder(name="NarutoShippuden", season="29"))
a.save()

ka = KindAnime(ka_anime=Anime.objects.get(name="Boku No Hero Academia", season=1),ka_kind=k)
ka.save()
ka = KindAnime(ka_anime=Anime.objects.get(name="Boku No Hero Academia", season=2),ka_kind=k2)
ka.save()

ka = KindAnime(ka_anime=Anime.objects.get(name="One Piece", season=1), ka_kind=k)
ka.save()

episode_filler(MIRROR_URI="www.onlyonepiece.cloud/", anime="One Piece")
episode_filler(MIRROR_URI="www.animeflex.cloud/", anime="Boku No Hero Academia", anime_season="5")
episode_filler(MIRROR_URI="www.brandnewanime.eu/", anime="Kuroko No Basket", anime_season="1")
episode_filler(MIRROR_URI="www.brandnewanime.eu/", anime="Kuroko No Basket", anime_season="2")
episode_filler(MIRROR_URI="www.brandnewanime.eu/", anime="Kuroko No Basket", anime_season="3")
episode_filler(MIRROR_URI="www.animeflex.cloud/", anime="Black Clover")
episode_filler(MIRROR_URI="www.onlyboruto.info/", anime="Naruto")
episode_filler(MIRROR_URI="www.onlyboruto.info/", anime="NarutoShippuden")
