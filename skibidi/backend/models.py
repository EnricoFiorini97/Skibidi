from typing import Protocol
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


class Kind(models.Model):
    kind_id = models.AutoField(primary_key=True)
    kind_name = models.CharField(max_length=255, null=False, unique=True)

    def __str__(self):
        return f"{self.kind_name}"

class Anime(models.Model):
    class Meta:
        unique_together = (('name', 'season'),)
    anime_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    plot = models.CharField(max_length=1000, null=True, blank=True)
    season = models.PositiveSmallIntegerField(null=False)
    last_episode = models.PositiveSmallIntegerField(null=False)
    start_number_episode = models.PositiveSmallIntegerField(null=False)
    global_rating = models.PositiveSmallIntegerField(null=True, blank=True)
    path = models.URLField(max_length=255, null=False)
    last_update = models.DateField(max_length=255, null=True, blank=True)
    autodownlodable = models.BooleanField(null=True, blank=True)
    finished = models.BooleanField(null=True, blank=True)
    img_source = models.CharField(max_length=255, null=False)

    def __str__(self):
        return f"{self.name} {self.season}"
    
class FavoritesKind(models.Model):
    class Meta:
        unique_together = (('fk_user', 'fk_kind'),)
    favorites_kind_id = models.AutoField(primary_key=True)
    fk_user = models.ForeignKey(User, related_name='fk_user', on_delete=CASCADE, null=False)
    fk_kind = models.ForeignKey(Kind, related_name='fk_kind', on_delete=CASCADE, null=False)

    def __str__(self):
        return f"{self.fk_user} {self.fk_kind}"
    
class FavoritesAnime(models.Model):
    class Meta:
        unique_together = (('fa_anime', 'fa_user'),)
    favorites_anime_id = models.AutoField(primary_key=True)
    fa_anime = models.ForeignKey(Anime, related_name='fa_anime',on_delete=CASCADE, null=False)
    fa_user = models.ForeignKey(User, related_name='fa_user', on_delete=CASCADE, null=False)

    def __str__(self):
        return f"{self.fa_anime} {self.fa_user}"

class Episode(models.Model):
    episode_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    seen = models.PositiveSmallIntegerField(null=False)
    e_anime = models.ForeignKey(Anime, related_name= 'e_anime',on_delete=CASCADE, null=False)
    path = models.URLField(null=False)

    def __str__(self):
        return f"{self.e_anime} {self.name}"


class Watching(models.Model):
    class Meta:
        unique_together = (('w_anime', 'w_user', 'w_episode'), )
    watching_id = models.AutoField(primary_key=True)
    w_user = models.ForeignKey(User, related_name='w_user', on_delete=CASCADE, null=False)
    w_anime = models.ForeignKey(Anime, related_name='w_anime', on_delete=CASCADE, null=False)
    w_episode = models.ForeignKey(Episode, related_name= 'w_episode',on_delete=CASCADE, null=False)
    seconds = models.PositiveSmallIntegerField(null=False, default=0) #TODO: convert to hh-mm-ss

    def __str__(self):
        return f"{self.w_episode}"

class UserRating(models.Model):
    class Meta:
        unique_together = (('ur_anime', 'ur_user'),)
    user_rating_id = models.AutoField(primary_key=True)
    ur_anime = models.ForeignKey(Anime, related_name='ur_anime', on_delete=CASCADE, null=False)
    ur_user = models.ForeignKey(User, related_name='ur_user' ,on_delete=CASCADE, null=False)
    rating = models.PositiveSmallIntegerField(null=False)
    def __str__(self):
        return f"{self.ur_anime} {self.ur_user}"

class KindAnime(models.Model):
    class Meta:
        unique_together = (('ka_anime', 'ka_kind'),)
    kind_anime_id = models.AutoField(primary_key=True)
    ka_anime = models.ForeignKey(Anime, related_name='ka_anime', on_delete=CASCADE, null=False)
    ka_kind = models.ForeignKey(Kind, related_name='ka_kind', on_delete=CASCADE, null=False)

    def __str__(self):
        return f"{self.ka_anime} {self.ka_kind}"

class PersonalKind(models.Model):
    class Meta:
        unique_together = (('p_user', 'p_kind'),)
    personal_kind_id = models.AutoField(primary_key=True)
    p_user = models.ForeignKey(User, related_name='p_user' ,on_delete=CASCADE, null=False)
    p_kind = models.ForeignKey(Kind, related_name='p_kind', on_delete=CASCADE, null=False)

    def __str__(self):
        return f"{self.p_kind}"