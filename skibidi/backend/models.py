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
    season = models.PositiveSmallIntegerField(null=False)
    num_episodes = models.PositiveSmallIntegerField(null=False)
    start_number_episode = models.PositiveSmallIntegerField(null=False)
    a_kind_id = models.ForeignKey(Kind, related_name='a_kind_id', on_delete=SET_DEFAULT, null=False, default=0)
    last_update = models.DateField()
    autodownlodable = models.BooleanField(null=False)
    finished = models.BooleanField(null=False)
    
class FavoritesKind(models.Model):
    class Meta:
        unique_together = (('fk_user_id', 'fk_kind_id'),)
    favorites_kind_id = models.AutoField(primary_key=True)
    fk_user_id = models.ForeignKey(User, related_name='fk_user_id', on_delete=CASCADE, null=False)
    fk_kind_id = models.ForeignKey(Kind, related_name='fk_kind_id', on_delete=CASCADE, null=False)
    
class FavoritesAnime(models.Model):
    class Meta:
        unique_together = (('fa_anime_id', 'fa_user_id'),)
    favorites_anime_id = models.AutoField(primary_key=True)
    fa_anime_id = models.ForeignKey(Anime, related_name= 'fa_anime_id',on_delete=CASCADE, null=False)
    fa_user_id = models.ForeignKey(User, related_name='fa_user_id', on_delete=CASCADE, null=False)
    
class Watching(models.Model):
    class Meta:
        unique_together = (('w_anime_id', 'w_user_id'),)
    watching_id = models.AutoField(primary_key=True)
    w_user_id = models.ForeignKey(User, related_name='w_user_id', on_delete=CASCADE, null=False)
    w_anime_id = models.ForeignKey(Anime, related_name='w_anime_id', on_delete=CASCADE, null=False)
    episode = models.PositiveSmallIntegerField(null=False)
    seconds = models.PositiveSmallIntegerField(null=False) #TODO: convert to hh-mm-ss

class UserRating(models.Model):
    class Meta:
        unique_together = (('ur_anime_id', 'ur_user_id'),)
    user_rating_id = models.AutoField(primary_key=True)
    ur_anime_id = models.ForeignKey(Anime, related_name='ur_anime_id', on_delete=CASCADE, null=False)
    ur_user_id = models.ForeignKey(User, related_name='ur_user_id' ,on_delete=CASCADE, null=False)
    rating = models.PositiveSmallIntegerField(null=False)