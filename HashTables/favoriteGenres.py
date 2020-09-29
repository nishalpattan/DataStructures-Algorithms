def favorite_genres(user_songs, song_genres):
    song_to_genre_map = dict()
    user_to_genre_map = dict()
    for genre in song_genres:
        for song in song_genres[genre]:
            song_to_genre_map[song] = genre

    for user in user_songs:
        # genre_set = set()
        _max = 0
        hash_map = dict()
        for user_song in user_songs[user]:
            genre = song_to_genre_map.get(user_song, "")
            hash_map[genre] = hash_map.get(genre, 0) + 1
            _max = max(_max, hash_map[genre])
            # if song_to_genre_map[user_song] not in genre_set:
            #     if user_to_genre_map.get(user, []) != []:
            #         user_to_genre_map[user].append(song_to_genre_map[user_song])
            #     else:
            #         user_to_genre_map[user] = [song_to_genre_map[user_song]]
            # genre_set.add(song_to_genre_map[user_song])
        for genre in hash_map:
            if hash_map.get(genre, 0) == _max:
                if user in user_to_genre_map:
                    user_to_genre_map[user].append(genre)
                else:
                    user_to_genre_map[user] = [genre]
    return user_to_genre_map







if __name__ == "__main__":

    # example 1
    user_songs = {
                    "David": ["song1", "song2", "song3", "song4", "song8"],
                    "Emma": ["song5", "song6", "song7"]
                }
    songe_genres = {
        "Rock": ["song1", "song3"],
        "Dubstep": ["song7"],
        "Techno": ["song2", "song4"],
        "Pop": ["song5", "song6"],
        "Jazz": ["song8", "song9"]
    }
    print(favorite_genres(user_songs, songe_genres))

    # example 2
    user_songs = {
                    "David": ["song1", "song2"],
                    "Emma": ["song3", "song4"]
                }
    song_genres = {}
    print(favorite_genres(user_songs, song_genres))
