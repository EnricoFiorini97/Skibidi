from backend.models import User, Kind, Anime,FavoritesKind,FavoritesAnime,Watching,UserRating

u = User(username="test", name="name", surname="smith")
u.save()

k = Kind(kind_name="shonen")
k.save()

a = Anime(name="One Piece", season = 1, num_episodes=977, start_number_episode=1, a_kind_id = k, last_update="2021-06-06", autodownlodable=True, finished=False)
a.save()

fk = FavoritesKind(fk_user_id=u, fk_kind_id=k)
fk.save()

fa = FavoritesAnime(fa_anime_id=a, fa_user_id=u)
fa.save()

w = Watching(w_user_id=u, w_anime_id=a, episode=1, seconds=134)
w.save()

ur = UserRating(ur_anime_id=a,ur_user_id=u,rating=4)
ur.save()

ki = Kind.objects.get(kind_name="shonen")
a = Anime(name="My Hero Academia", season=1, num_episodes=13, start_number_episode=1, a_kind_id = ki, last_update="2016-06-26",autodownlodable=False, finished = True)
a.save()
a = Anime(name="My Hero Academia", season=2, num_episodes=26, start_number_episode=0, a_kind_id = ki, last_update="2017-09-30",autodownlodable=False, finished = True)
a.save()
a = Anime(name="My Hero Academia", season=3, num_episodes=25, start_number_episode=1, a_kind_id = ki, last_update="2018-09-29",autodownlodable=False, finished = True)
a.save()
a = Anime(name="My Hero Academia", season=4, num_episodes=25, start_number_episode=1, a_kind_id = ki, last_update="2020-04-04",autodownlodable=False, finished = True)
a.save()
a = Anime(name="My Hero Academia", season=5, num_episodes=11, start_number_episode=1, a_kind_id = ki, last_update="2021-06-05",autodownlodable=False, finished = False)
a.save()