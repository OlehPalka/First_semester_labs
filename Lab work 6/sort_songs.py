"""
Sorting songs by different parametres
"""
def song_length(song_titles_and_length_songs: tuple) -> int:
    """
    This function returns float number of the song length.

    >>> song_length(('c mnabs gjfd', '5'))
    5
    """
    #create key for lenth of songs
    return int(song_titles_and_length_songs[1])

def title_length(song_titles_and_length_songs):
    """
    This function returns song names length.

    >>> title_length(('c mnabs gjfd', '5'))
    12
    """
    #create key for sorting songs by their lenth
    result = len(song_titles_and_length_songs[0])
    return result

def last_word(song_titles_and_length_songs):
    """
    This function returns first letter of the last word from name of the song.

    >>> last_word(('c mnabsgjfd', '5'))
    'm'
    """
    #create key for sorting songs by last word of title
    last_name_word = song_titles_and_length_songs[0]
    last_name_word = last_name_word.split()
    last_name_word = last_name_word[-1]
    first_letter_of_lastword = last_name_word[0]
    return first_letter_of_lastword

def sort_songs(song_titles, length_songs, key):
    """
    (list, list,key) -> list
    This function sorts sngs by songs using keyes for sorting from other functions.
    If there are more or less lengthes of songs than titles of songs,
    function returns None

    >>> sort_songs(["a b", "c", "d e", "f"], ['3', '5', '8'], key = last_word)
    >>> sort_songs(["a b", "c", "d e", "f"], ['3', '5', '8', '10'], key = last_word)
    [('a b', '3'), ('c', '5'), ('d e', '8'), ('f', '10')]
    >>> sort_songs(["a b", "c", "d e", "f"], ['3', '5', '8', '10'], key = title_length)
    [('c', '5'), ('f', '10'), ('a b', '3'), ('d e', '8')]
    >>> sort_songs(["a b", "c", "d e", "f"], ['3', '5', '8', '10'], key = song_length)
    [('a b', '3'), ('c', '5'), ('d e', '8'), ('f', '10')]
    """
    # sort songs with usage of keys
    if len(song_titles) != len(length_songs):
        song_titles_and_length_songs = None
    else:
        song_titles_and_length_songs = zip(song_titles, length_songs)
        song_titles_and_length_songs = sorted(song_titles_and_length_songs, key = key)

    return song_titles_and_length_songs
