def get_all_anime_name_and_seasons():
    ''' Returns anime name, anime season, total episodes, starting episode '''
    return f"SELECT A.name, A.season, A.num_episodes, A.start_number_episode FROM 'backend_anime' as A"

def get_specific_anime_by_name(name="One Piece"):
    '''Given a general anime name (no season specified), returns anime name, anime season, 
       total episodes, starting episode of all seasons '''
    return f"SELECT A.name, A.season, A.num_episodes, A.start_number_episode FROM 'backend_anime' as A WHERE A.name LIKE '%{name}%'"