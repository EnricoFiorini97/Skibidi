import sqlite3
import os
import json
from django.http.response import Http404
from . import queries
from pathlib import Path
from os.path import dirname
from http import HTTPStatus
from backend.errors import DBErrors
from rest_framework import serializers

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


class KindSerializer(serializers.Serializer):
    kind_id = serializers.IntegerField()
    kind_name = serializers.CharField(max_length = 255)

class FavoritesKindSerializer(serializers.Serializer):
    favorites_kind_id = serializers.IntegerField()
    fk_user = serializers.IntegerField()
    fk_kind = serializers.IntegerField()


def __json_db_query_serialize(status=HTTPStatus.OK, body=""):
    return json.dumps({
        "status":status,
        "body":body
    })


def serialize_all_anime_to_json():
    return custom_query(queries.get_all_anime_name_and_seasons())


def serialize_anime_by_name_to_json(name="One Piece"):
    return custom_query(queries.get_specific_anime_by_name(name))


def serialize_anime_by_kind_to_json(kind="shonen"):
    return custom_query(queries.get_all_anime_by_kind(kind))


def serialize_anime_by_global_rating_to_json():
    return custom_query(queries.get_all_anime_by_global_rating())


def serialize_anime_by_global_rating_and_kind_to_json(kind="shonen"):
    return custom_query(queries.get_all_anime_by_global_rating_and_kind(kind))


def serialize_all_distinct_titles_to_json():
    return custom_query(queries.get_all_distinct_titles())


def serialize_season_by_anime_name_to_json(anime="One Piece"):
    return custom_query(queries.get_seasons_count_by_anime_name(anime))

   
def custom_query(query):
    if query is None or query.strip() == "":
        return __json_db_query_serialize(status=HTTPStatus.INTERNAL_SERVER_ERROR, body=DBErrors.MSG_QUERY_SYNTAX_ERROR)

    try:
        path = dirname(dirname(Path(os.path.realpath(__file__))))
        sqliteConnection = sqlite3.connect(path + os.path.sep + 'db.sqlite3')
        sqliteConnection.row_factory = sqlite3.Row
        cursor = sqliteConnection.cursor()
        cursor.execute(query)
        record = [dict(r) for r in cursor.fetchall()]
        cursor.close()
        return __json_db_query_serialize(body=record)
    except sqlite3.OperationalError:
        return __json_db_query_serialize(status=HTTPStatus.INTERNAL_SERVER_ERROR, body=DBErrors.MSG_QUERY_SYNTAX_ERROR)
    except sqlite3.Error:
        return __json_db_query_serialize(status=HTTPStatus.INTERNAL_SERVER_ERROR, body=DBErrors.MSG_INVALID_PATH)
