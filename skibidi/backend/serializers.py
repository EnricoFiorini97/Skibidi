from rest_framework import serializers
from backend.models import  Kind, Anime, Episode
from django.contrib.auth import get_user_model


class AnimeSerializer(serializers.Serializer):
    anime_id = serializers.IntegerField()
    name = serializers.CharField(max_length = 255)
    plot = serializers.CharField(max_length = 1000)
    season = serializers.IntegerField()
    last_episode = serializers.IntegerField()
    start_number_episode = serializers.IntegerField()
    global_rating = serializers.IntegerField()
    last_update = serializers.DateField()
    autodownlodable = serializers.BooleanField()
    finished = serializers.BooleanField()
    img_source = serializers.CharField(max_length = 1000)


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField(max_length = 255)
    email = serializers.CharField(max_length = 255)
    first_name = serializers.CharField(max_length = 255)
    last_name = serializers.CharField(max_length = 255)
    password = serializers.CharField(max_length = 255)

class KindSerializer(serializers.Serializer):
    kind_id = serializers.IntegerField()
    kind_name = serializers.CharField(max_length = 255)


class FavoritesKindSerializer(serializers.Serializer):
    favorites_kind_id = serializers.IntegerField()
    fk_user = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())
    fk_kind = serializers.PrimaryKeyRelatedField(queryset=Kind.objects.all())


class FavoritesAnimeSerializer(serializers.Serializer):
    favorites_anime_id = serializers.IntegerField()
    fa_anime = serializers.PrimaryKeyRelatedField(queryset=Anime.objects.all())
    fa_user = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())


class WatchingSerializer(serializers.Serializer):
    watching_id = serializers.IntegerField()
    w_user = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())
    w_anime = serializers.PrimaryKeyRelatedField(queryset=Anime.objects.all())
    w_episode = serializers.PrimaryKeyRelatedField(queryset=Episode.objects.all())
    seconds = serializers.IntegerField()


class UserRatingSerializer(serializers.Serializer):
    user_rating_id = serializers.IntegerField()
    ur_anime = serializers.PrimaryKeyRelatedField(queryset=Anime.objects.all())
    ur_user = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())
    rating = serializers.IntegerField()


class KindAnimeSerializer(serializers.Serializer):
    kind_anime_id = serializers.IntegerField()
    ka_anime = serializers.PrimaryKeyRelatedField(queryset=Anime.objects.all())
    ka_kind = serializers.PrimaryKeyRelatedField(queryset=Kind.objects.all())


class EpisodeSerializer(serializers.Serializer):
    episode_id = serializers.IntegerField()
    name = serializers.CharField(max_length = 255)
    seen = serializers.IntegerField()
    e_anime = serializers.PrimaryKeyRelatedField(queryset=Anime.objects.all())
    path = serializers.URLField()