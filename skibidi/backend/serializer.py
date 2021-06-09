import sqlite3
import os
import json
from django.http.response import Http404
from . import queries
from pathlib import Path
from os.path import dirname
from http import HTTPStatus
from backend.errors import DBErrors

def __json_db_query_serialize(status=HTTPStatus.OK, body=""):
    return json.dumps({
        "status":status,
        "body":body
    })

def serialize_all_anime_to_json():
    return custom_query(queries.get_all_anime_name_and_seasons())

def serialize_anime_by_name_to_json(name="One Piece"):
    return custom_query(queries.get_specific_anime_by_name(name))
   
def custom_query(query):
    if query is None or query.strip() == "":
        raise ValueError("Query must be a non-empty string.")
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
