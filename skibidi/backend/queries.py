def get_all_anime_name_and_seasons():
    ''' Returns anime name, anime season, total episodes, starting episode '''
    return f"SELECT A.name, A.season, A.last_episode, A.start_number_episode FROM 'backend_anime' as A"


def get_specific_anime_by_name(name="One Piece"):
    '''Given a general anime name (no season specified), returns anime name, anime season, 
       total episodes, starting episode of all seasons '''
    return f"SELECT A.name, A.season, A.last_episode, A.start_number_episode FROM 'backend_anime' as A WHERE A.name LIKE '%{name}%'"


def get_all_anime_by_kind(kind="shonen"):
    '''Given a kind returns anime name, anime season, 
       total episodes, starting episode of all seasons matching that kind'''
    return f"SELECT A.name, A.season FROM 'backend_anime' as A, 'backend_kind' as K, 'backend_kindanime' as KA WHERE K.kind_name = '{kind}' AND K.kind_id = KA.ka_kind_id AND A.anime_id = KA.ka_anime_id"


def get_all_anime_by_global_rating():
    ''' Returns anime name, anime season, total episodes, starting episode ordered by decreasing rating'''
    return f"SELECT A.name, A.season, A.global_rating FROM 'backend_anime' as A ORDER BY A.global_rating DESC"


def get_all_anime_by_global_rating_and_kind(kind="shonen"):
    return f"SELECT A.name, A.season, A.global_rating FROM 'backend_anime' as A, 'backend_kind' as K, 'backend_kindanime' as KA WHERE K.kind_name = '{kind}' AND K.kind_id = KA.ka_kind_id AND A.anime_id = KA.ka_anime_id ORDER BY A.global_rating DESC"


def get_all_distinct_titles():
    return f"SELECT DISTINCT A.name FROM 'backend_anime' as A"


def get_seasons_count_by_anime_name(name="My Hero Academia"):
    return f"SELECT A1.name, A1.season, A1.last_episode, A1.start_number_episode FROM 'backend_anime' as A1 WHERE A1.name = '{name}' GROUP BY A1.name, A1.season"