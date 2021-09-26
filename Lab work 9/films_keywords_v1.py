"""
This module makes operations with films and their keywords.
"""


def find_film_keywords(film_keywords: dict, film_name: str) -> set:
    """
    This function returns set of key words for filmname.

    >>> print(find_film_keywords({"vampire": ["Rozario to banp\
aia", "Monoliza"], "roll": ["Sanctuary", "Rozario to banpaia"], "s\
pace": ["Alien"]}, "Alien"))
    {'space'}
    """
    return {word[1] for word in enumerate(
        film_keywords) if film_name in film_keywords[word[1]]}


def find_films_with_keywords(film_keywords: dict, num_of_films: int) -> dict:
    """
    This function returns dictionary of films which have the
    biggest amount of key words.

    >>> print(find_films_with_keywords({"vampire": ["Rozario to b\
anpaia", "Monoliza"], "roll": ["Sanctuary", "Rozario to banpai\
a"], "space": ["Alien"]}, 1))
    [('Rozario to banpaia', 2)]
    """
    films_dict = dict()
    for film_list in film_keywords.values():
        for film in film_list:
            if film not in films_dict:
                films_dict[film] = 1
            else:
                films_dict[film] += 1
    list_for_sorting = list(films_dict.items())
    list_for_sorting.sort(key=lambda i: i[0])
    list_for_sorting.sort(key=lambda i: i[1])
    list_for_sorting.reverse()

    return list_for_sorting[:num_of_films]
