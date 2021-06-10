from django.db import models
from django.db.models.deletion import CASCADE, SET_DEFAULT, SET_NULL

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length = 255, null=False, unique=True)
    name = models.CharField(max_length = 255, null=False)
    surname = models.CharField(max_length = 255, null=False)
    
class Kind(models.Model):
    kind_id = models.AutoField(primary_key=True)
    kind_name = models.CharField(max_length = 255, null=False, unique=True)

class Anime(models.Model):
    class Meta:
        unique_together = (('name', 'season'),)
    anime_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 255, null=False)
    plot = models.CharField(max_length = 1000, null=True)
    season = models.PositiveSmallIntegerField(null=False)
    last_episode = models.PositiveSmallIntegerField(null=False)
    start_number_episode = models.PositiveSmallIntegerField(null=False)
    global_rating = models.PositiveSmallIntegerField(null=True)
    path = models.FilePathField(null=True)
    last_update = models.DateField()
    autodownlodable = models.BooleanField(null=True)
    finished = models.BooleanField(null=True)
    
class FavoritesKind(models.Model):
    class Meta:
        unique_together = (('fk_user', 'fk_kind'),)
    favorites_kind_id = models.AutoField(primary_key=True)
    fk_user = models.ForeignKey(User, related_name='fk_user', on_delete=CASCADE, null=False)
    fk_kind = models.ForeignKey(Kind, related_name='fk_kind', on_delete=CASCADE, null=False)
    
class FavoritesAnime(models.Model):
    class Meta:
        unique_together = (('fa_anime', 'fa_user'),)
    favorites_anime_id = models.AutoField(primary_key=True)
    fa_anime = models.ForeignKey(Anime, related_name= 'fa_anime',on_delete=CASCADE, null=False)
    fa_user = models.ForeignKey(User, related_name='fa_user', on_delete=CASCADE, null=False)
    
class Watching(models.Model):
    class Meta:
        unique_together = (('w_anime', 'w_user'),)
    watching_id = models.AutoField(primary_key=True)
    w_user = models.ForeignKey(User, related_name='w_user', on_delete=CASCADE, null=False)
    w_anime = models.ForeignKey(Anime, related_name='w_anime', on_delete=CASCADE, null=False)
    episode = models.PositiveSmallIntegerField(null=False)
    seconds = models.PositiveSmallIntegerField(null=False, default=0) #TODO: convert to hh-mm-ss

class UserRating(models.Model):
    class Meta:
        unique_together = (('ur_anime', 'ur_user'),)
    user_rating_id = models.AutoField(primary_key=True)
    ur_anime = models.ForeignKey(Anime, related_name='ur_anime', on_delete=CASCADE, null=False)
    ur_user = models.ForeignKey(User, related_name='ur_user' ,on_delete=CASCADE, null=False)
    rating = models.PositiveSmallIntegerField(null=False)

class KindAnime(models.Model):
    class Meta:
        unique_together = (('ka_anime', 'ka_kind'),)
    kind_anime_id = models.AutoField(primary_key=True)
    ka_anime = models.ForeignKey(Anime, related_name='ka_anime', on_delete=CASCADE, null=False)
    ka_kind = models.ForeignKey(Kind, related_name='ka_kind', on_delete=CASCADE, null=False)